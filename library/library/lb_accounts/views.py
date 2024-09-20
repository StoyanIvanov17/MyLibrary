from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, logout, authenticate

from library.lb_accounts.forms import LibraryUserCreationForm
from library.lb_accounts.utils.library_card_number_generator import generate_library_card_number


class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/signin_user.html'
    redirect_authenticated_user = True


class SignUpUserView(views.CreateView):
    template_name = 'accounts/signup_user.html'
    form_class = LibraryUserCreationForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.library_card_number = generate_library_card_number()
        user.save()

        login(self.request, form.instance)
        return super().form_valid(form)


def signout_user(request):
    logout(request)
    return redirect('home page')
