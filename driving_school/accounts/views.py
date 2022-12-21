from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView

from driving_school.accounts.forms import UserCreateForm

UserModel = get_user_model()


class RegisterUserView(CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class LogInUserView(LoginView):
    template_name = 'accounts/login-page.html'



class LogOutUserView(LogoutView):
    next_page = reverse_lazy('index')


class EditUserView(UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email')
    success_url = reverse_lazy('details user')


class DeleteUserView(DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')


class DetailUserView(DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel
