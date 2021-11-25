from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import *
from django.urls import reverse, reverse_lazy

"""URL функции"""

class Homepage(ListView):
    model = TWEET
    template_name = 'twt/home.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

class ShowPost(DetailView):
    model = TWEET
    template_name = 'twt/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    slug_field = 'pk'


class Addpost(CreateView):
    form_class = AddPostForm
    template_name = 'twt/addpost.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить пост'
        return context


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'twt/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'twt/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('home')


def info(request):
    return render(request, 'twt/info.html', {'title': 'Информация'})

