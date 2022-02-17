from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "User Name"})
    )
    email = forms.EmailField(
        required=True,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Email"})
    )
    password = forms.CharField(
        required=True,
        label=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    password2 = forms.CharField(
        required=True,
        label=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "User Name"})
    )
    password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
