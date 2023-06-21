from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Введите никнейм'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input', 'placeholder': 'Введите пароль'}
    ))

    class Meta:
        model = User
        fields = ['username', 'password']


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Придумайте никнейм'}
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input', 'placeholder': 'Придуймайте пароль'}
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input', 'placeholder': 'Повторите пароль'}
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'input', 'placeholder': 'Введите адрес почты'}
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
