from django.core.validators import MinValueValidator, RegexValidator
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from taxi.models import Driver, Car


class CarCreationForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    drivers = forms.ModelMultipleChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "license_number",
            "first_name",
            "last_name",
            "email",
        )


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["license_number"]
