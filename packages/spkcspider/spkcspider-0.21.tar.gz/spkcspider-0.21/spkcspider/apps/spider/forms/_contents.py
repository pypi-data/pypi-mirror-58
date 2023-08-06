__all__ = [
    "LinkForm", "TravelProtectionForm", "TravelProtectionManagementForm"
]

from base64 import b64encode
from datetime import timedelta

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

from django import forms
from django.conf import settings
from django.contrib.auth import authenticate
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from spkcspider.constants import (
    TravelLoginType, VariantType, dangerous_login_choices,
    loggedin_active_tprotections, travel_scrypt_params
)
from spkcspider.utils.settings import get_settings_func

from ..fields import ContentMultipleChoiceField, MultipleOpenChoiceField
from ..models import AssignedContent, LinkContent, TravelProtection
from ..widgets import (
    OpenChoiceWidget, DatetimePickerWidget, SelectizeWidget
)
from ._messages import time_help_text, login_protection

_extra = '' if settings.DEBUG else '.min'


class LinkForm(forms.ModelForm):
    content = forms.ModelChoiceField(
        queryset=AssignedContent.objects.filter(
            strength__lte=10
        )
    )

    class Meta:
        model = LinkContent
        fields = ['push']

    def __init__(self, uc, request, **kwargs):
        super().__init__(**kwargs)
        # if self.instance.associated:
        #     if "\x1eanchor\x1e" in self.instance.associated:
        #         self.fields["content"].disabled = True
        if self.instance.id:
            self.initial["content"] = \
                self.instance.associated.attached_to_content
        q = self.fields["content"].queryset
        travel = TravelProtection.objects.get_active_for_request(request)
        travel = travel.filter(
            login_protection__in=loggedin_active_tprotections
        )
        self.fields["content"].queryset = q.filter(
            strength__lte=uc.strength
        ).exclude(
            models.Q(usercomponent__travel_protected__in=travel) |
            models.Q(travel_protected__in=travel)
        )
        # component auth should limit links to visible content
        # read access outside from component elsewise possible
        if request.user != uc.user and not request.is_staff:
            q = self.fields["content"].queryset
            self.fields["content"].queryset = q.filter(
                models.Q(usercomponent=uc) |
                models.Q(referenced_by__usercomponent=uc)
            )

    def save(self, commit=True):
        self.instance.associated.attached_to_content = \
            self.cleaned_data["content"]
        return super().save(commit)


class TravelProtectionManagementForm(forms.ModelForm):
    class Meta:
        model = TravelProtection
        fields = []

    def clean(self):
        super().clean()
        pwset = set(self.instance.associated.getlist("pwhash", 20))
        self.instance._encoded_form_info = "".join(
            map(lambda x: "pwhash={}\x1e".format(x), pwset)
        )
        if self.instance.associated.getflag("anonymous_deactivation"):
            self.instance._encoded_form_info = \
                "{}anonymous_deactivation\x1e".format(
                    self.instance._encoded_form_info
                )
        if self.instance.associated.getflag("anonymous_trigger"):
            self.instance._encoded_form_info = \
                "{}anonymous_trigger\x1e".format(
                    self.instance._encoded_form_info
                )

        return self.cleaned_data


class TravelProtectionForm(forms.ModelForm):
    uc = None
    # self_protection = forms.ChoiceField(
    #    label=_("Self-protection"), help_text=_(_self_protection),
    #     initial="None", choices=PROTECTION_CHOICES
    # )
    start = forms.DateTimeField(
        required=True, widget=DatetimePickerWidget(),
        help_text=time_help_text
    )
    stop = forms.DateTimeField(
        required=False, widget=DatetimePickerWidget(),
        help_text=time_help_text
    )
    trigger_pws = MultipleOpenChoiceField(
        label=_("Trigger Passwords"), required=False,
        widget=OpenChoiceWidget(
            allow_multiple_selected=True,
            attrs={
                "style": "min-width: 250px; width:100%"
            }
        )
    )
    approved = forms.BooleanField(disabled=True)
    overwrite_pws = forms.BooleanField(
        required=False, initial=False,
        help_text=_(
            "If set, the set of passwords is overwritten or "
            "removed (if no passwords are set)"
        )
    )
    anonymous_deactivation = forms.BooleanField(
        required=False, initial=False,
        help_text=_(
            "Can deactivate protection without login"
        )
    )
    protect_contents = ContentMultipleChoiceField(
        queryset=AssignedContent.objects.all(), required=False,
        to_field_name="id",
        widget=SelectizeWidget(
            allow_multiple_selected=True,
            attrs={
                "style": "min-width: 250px; width:100%"
            }
        )
    )

    master_pw = forms.CharField(
        label=_("Master Login Password"),
        widget=forms.PasswordInput(render_value=True), required=True
    )

    class Meta:
        model = TravelProtection
        fields = [
            "active", "start", "stop", "login_protection",
            "protect_components", "protect_contents", "trigger_pws"
        ]
        widgets = {
            "protect_components": SelectizeWidget(
                 allow_multiple_selected=True,
                 attrs={
                     "style": "min-width: 250px; width:100%"
                 }
            )
        }
        help_texts = {
            "login_protection": login_protection,
            "master_pw": _(
                "Enter Password used for the user account"
            )
        }

    class Media:
        js = []

    @classmethod
    def _filter_selfprotection(cls, x):
        if x[0] == TravelLoginType.disable:
            return False
        return True

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        if self.instance.associated.ctype.name == "TravelProtection":
            self.fields["start"].help_text = str(
                self.fields["start"].help_text
            ).format(timezone.get_current_timezone_name())
            self.fields["stop"].help_text = str(
                self.fields["stop"].help_text
            ).format(timezone.get_current_timezone_name())
            if not getattr(self.instance, "id"):
                now = timezone.now()
                self.initial["start"] = now + timedelta(hours=3)
                self.initial["stop"] = now + timedelta(days=7)
        else:
            self.fields["login_protection"].choices = \
                filter(
                    self._filter_selfprotection,
                    self.fields["login_protection"].choices
                )
            del self.fields["start"]
            del self.fields["stop"]
        if not getattr(self.instance, "id") and not self.data:
            self.initial["active"] = True

        travel = TravelProtection.objects.get_active_for_request(
            request
        ).filter(login_protection__in=loggedin_active_tprotections)
        selfid = getattr(self.instance, "id", -1)
        if self.initial["login_protection"] not in dangerous_login_choices:
            del self.fields["approved"]
        if self.initial["login_protection"] == TravelLoginType.disable:
            self.initial["login_protection"] = \
                TravelLoginType.trigger_disable

        q_component = models.Q(
            user=request.user
        ) & (
            ~models.Q(travel_protected__in=travel) |
            models.Q(travel_protected__id=selfid)
        )
        self.fields["protect_components"].queryset = \
            self.fields["protect_components"].queryset.filter(
                q_component
            ).distinct().order_by(
                "name"
            )

        q_content = models.Q(usercomponent__user=request.user) & (
            ~(
                models.Q(usercomponent__travel_protected__in=travel) |
                models.Q(travel_protected__in=travel) |
                # don't allow detectable contents
                models.Q(info__contains="\x1eanchor\x1e") |
                models.Q(info__contains="\x1eprimary\x1e") |
                # contents also appearing as features are easily detectable
                models.Q(
                    ctype__ctype__contains=VariantType.feature_connect
                )
            ) |
            (
                models.Q(usercomponent__travel_protected__id=selfid) |
                models.Q(travel_protected__id=selfid)
            )
        )
        if getattr(self.instance, "id", None):
            # exlude own content
            q_content &= ~models.Q(pk=self.instance.associated.pk)
            self.initial["anonymous_deactivation"] = \
                self.instance.associated.getflag("anonymous_deactivation")
            if self.instance.associated.getlist("pwhash", 1):
                self.fields["trigger_pws"].help_text = _(
                    "<span style='color:red'>Trigger passwords already set."
                    "</span>"
                )
            else:
                self.fields["trigger_pws"].help_text = _(
                    "No trigger passwords set."
                )
                del self.fields["overwrite_pws"]
        if (
            not self.instance.associated.getlist("pwhash", 1) and
            self.instance.associated.ctype.name == "SelfProtection"
        ):
            self.fields["trigger_pws"].required = True
        # use q for filtering (including own)
        self.fields["protect_contents"].queryset = \
            self.fields["protect_contents"].queryset.filter(
                q_content
            ).distinct().order_by(
                "name"
            )

    def clean(self):
        super().clean()
        self.initial["master_pw"] = self.cleaned_data.pop("master_pw", None)
        if not authenticate(
            self.request,
            username=self.instance.associated.usercomponent.username,
            password=self.initial.get("master_pw", None),
            nospider=True
        ):
            self.add_error(
                "master_pw",
                forms.ValidationError(
                    _("Invalid Password"),
                    code="invalid_password"
                )
            )
        if "trigger_pws" in self.cleaned_data:
            pwset = set(map(
                lambda x: b64encode(Scrypt(
                    salt=settings.SECRET_KEY.encode("utf-8"),
                    backend=default_backend(),
                    **travel_scrypt_params
                ).derive(x[:128].encode("utf-8"))).decode("ascii"),
                self.cleaned_data["trigger_pws"]
            ))
            if (
                self.instance.associated.ctype.name == "SelfProtection" and
                self.cleaned_data.get("overwrite_pws") and
                len(pwset) == 0
            ):
                self.add_error("trigger_pws", forms.ValidationError(
                    _(
                        "Clearing trigger passwords not allowed "
                        "(for Self-Protection)"
                    )
                ))
            if not self.cleaned_data.get("overwrite_pws") and len(pwset) < 20:
                pwset.update(self.instance.associated.getlist(
                    "pwhash", 20-len(pwset)
                ))
        else:
            pwset = set(self.instance.associated.getlist("pwhash", 20))
        self.instance._encoded_form_info = "".join(
            map(lambda x: "pwhash={}\x1e".format(x), pwset)
        )
        if self.cleaned_data.get("start") and self.cleaned_data.get("stop"):
            if self.cleaned_data["stop"] < self.cleaned_data["start"]:
                self.add_error("start", forms.ValidationError(
                    _("Stop < Start")
                ))
        if self.cleaned_data.get("anonymous_deactivation"):
            self.instance._encoded_form_info = \
                "{}anonymous_deactivation\x1e".format(
                    self.instance._encoded_form_info
                )
        if self.cleaned_data.get("anonymous_trigger"):
            self.instance._encoded_form_info = \
                "{}anonymous_trigger\x1e".format(
                    self.instance._encoded_form_info
                )
        if self.cleaned_data["login_protection"] in dangerous_login_choices:
            self.cleaned_data["approved"] = get_settings_func(
                "SPIDER_DANGEROUS_APPROVE",
                "spkcspider.apps.spider.functions.approve_dangerous"
            )(self)
            if self.cleaned_data["approved"] is False:
                self.add_error("login_protection", forms.ValidationError(
                    _("This login protection is not allowed")
                ))
        else:
            self.cleaned_data["approved"] = True
        try:
            self.cleaned_data["protect_contents"] = \
                self.cleaned_data["protect_contents"].exclude(
                    usercomponent__in=self.cleaned_data["protect_components"]
                )
        except KeyError:
            pass
        return self.cleaned_data

    def is_valid(self):
        isvalid = super().is_valid()
        if not getattr(self, "cleaned_data", None):
            return False
        return isvalid

    def _save_m2m(self):
        super()._save_m2m()
        self.instance.protect_contents.add(self.instance.associated)

    def save(self, commit=True):
        self.instance.approved = bool(self.cleaned_data["approved"])
        return super().save(commit)
