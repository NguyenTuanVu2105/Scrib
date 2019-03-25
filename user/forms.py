from django.forms import forms

class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))