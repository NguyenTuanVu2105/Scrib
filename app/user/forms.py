from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']