
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = TWEET
        fields = '__all__'


class RegisterUserForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update(
        {
            "duplicate_username": (
                "This username has already been taken."
            )
        }
    )

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', )



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
