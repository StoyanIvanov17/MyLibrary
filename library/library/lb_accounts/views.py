from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, logout

from library.lb_accounts.forms import LibraryCardAuthenticationForm, LibraryUserCreationForm


class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/signin_user.html'
    redirect_authenticated_user = True
    form_class = LibraryCardAuthenticationForm


class SignUpUserView(views.CreateView):
    template_name = 'accounts/signup_user.html'
    form_class = LibraryUserCreationForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, form.instance)

        return result


def signout_user(request):
    logout(request)
    return redirect('home page')
