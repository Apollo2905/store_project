from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .bulma_mixin import BulmaMixin


class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Напишите никнейм')
    password = forms.CharField(widget=forms.PasswordInput(), label='Напишите пароль')

    class Meta:
        model = User
        fields = ['username', 'password']


class SignUpForm(BulmaMixin, UserCreationForm):
    username = forms.CharField(label='Придумайте никнейм')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Придумайте пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль')
    email = forms.CharField(widget=forms.EmailInput(), label='Напишите адрес почты')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
