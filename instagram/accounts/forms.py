from django.contrib.auth.models import User
from django import forms
from django.db.transaction import commit
from django.forms import widgets

from accounts.models import Profile


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput
    )

    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        strip=False
    )

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Password do not confirm')
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'email']


class UserChangeForm(forms.ModelForm):
    avatar = forms.ImageField(
        required=True
    )

    about_me = forms.CharField(
        required=False,
        widget=widgets.Textarea,
        max_length=1000
    )

    phone_number = forms.CharField(
        required=False,
        max_length=12,
    )

    gender = forms.ChoiceField(
        required=False,
        choices=(('male', 'male'), ('female', 'female'))
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        profile_fields = ['avatar', 'phone_number', 'about_me', 'gender']

    def save(self):
        user = super().save(commit)
        self.save_profile(commit)
        return user

    def save_profile(self, commit=True):
        try:
            profile = self.instance.profile
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=self.instance)

        for field in self.Meta.profile_fields:
            setattr(profile, field, self.cleaned_data[field])

        if not profile.avatar:
            profile.avatar = None

        if commit:
            profile.save()

    def get_initial_for_field(self, field, field_name):
        if field_name in self.Meta.profile_fields:
            try:
                return getattr(self.instance.profile, field_name)
            except Profile.DoesNotExist:
                return None

        return super().get_initial_for_field(field, field_name)