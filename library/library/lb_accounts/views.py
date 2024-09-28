from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, logout, authenticate

from library.lb_accounts.forms import LibraryUserCreationForm, LibraryProfileForm
from library.lb_accounts.models import LibraryProfile
from library.lb_accounts.utils.library_card_number_generator import generate_library_card_number


class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/signin_user.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        # Redirect to the user's profile page after login
        user = self.request.user
        if user.is_authenticated and hasattr(user, 'libraryprofile'):
            return reverse("account details", kwargs={"pk": user.libraryprofile.pk})
        # Optionally, you can set a default URL if there's no profile
        return super().get_success_url()


from django.core.exceptions import ValidationError


class SignUpUserView(views.CreateView):
    template_name = 'accounts/signup_user.html'
    form_class = LibraryUserCreationForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.library_card_number = generate_library_card_number()
        user.save()

        # Create the profile here, without using get_or_create
        try:
            profile = LibraryProfile.objects.create(
                user=user,
                email=user.email,  # Use the user's email for the profile
            )
            login(self.request, user)  # Log the user in if the profile is created
            return redirect('registration profile')  # Redirect to the profile creation form
        except IntegrityError:
            # If there’s an integrity error, handle it here (e.g., log it or redirect)
            return redirect('account details')  # Redirect or handle the error as needed


class LibraryProfileCreateView(LoginRequiredMixin, views.UpdateView):
    model = LibraryProfile
    form_class = LibraryProfileForm
    template_name = 'accounts/profile-registration.html'
    success_url = reverse_lazy('account details')

    def get_success_url(self):
        return reverse_lazy('account details', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        # Ensure the profile is created for the logged-in user
        profile, created = LibraryProfile.objects.get_or_create(user=self.request.user)
        return profile


def signout_user(request):
    logout(request)
    return redirect('home page')


class AccountDetailsView(views.DetailView):
    queryset = LibraryProfile.objects.all()
    template_name = 'accounts/account_details.html'


class AccountUpdateView(views.UpdateView):
    queryset = LibraryProfile.objects.all()
    template_name = 'accounts/account_update.html'
    form_class = LibraryProfileForm

    def get_success_url(self):
        return reverse("account details", kwargs={
            "pk": self.object.pk,
        })