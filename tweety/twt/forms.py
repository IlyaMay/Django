from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = TWEET
        fields = '__all__'


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label=('Ваш логин'), max_length=12,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    first_name = forms.CharField(label=('Ваше имя'), max_length=12, min_length=3,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    last_name = forms.CharField(label=('Ваша фамилия'), max_length=12, min_length=3 ,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))
    password1 = forms.CharField(label=('Введите Пароль'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label=('Повторите пароль'),widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    email = forms.EmailField(label=('Ваш email'),widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Еmail'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email',)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
