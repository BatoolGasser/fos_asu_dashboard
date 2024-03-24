from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="username", required=True)
    password = forms.CharField(max_length=100, label="password", widget=forms.PasswordInput, required=True)