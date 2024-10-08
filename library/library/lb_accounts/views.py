from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, logout

from library.lb_accounts.forms import LibraryUserCreationForm, LibraryProfileForm
from library.lb_accounts.models import LibraryProfile
from library.lb_accounts.utils.library_card_number_generator import generate_library_card_number


class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/signin_user.html'
    redirect_authenticated_user = True

    def get_success_url(self):

        user = self.request.user
        if user.is_authenticated and hasattr(user, 'libraryprofile'):
            return reverse("account details", kwargs={"pk": user.libraryprofile.pk})

        return super().get_success_url()


class SignUpUserView(views.CreateView):
    template_name = 'accounts/signup_user.html'
    form_class = LibraryUserCreationForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.library_card_number = generate_library_card_number()
        user.save()

        try:
            profile = LibraryProfile.objects.create(
                user=user,
                email=user.email,
            )
            login(self.request, user)
            return redirect('registration profile')
        except IntegrityError:

            try:
                profile = LibraryProfile.objects.get(user=user)
                return redirect('account details', pk=profile.pk)
            except LibraryProfile.DoesNotExist:
                return redirect('home page')


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()  # current profile
        context['saved_items'] = profile.saved_items.all()
        context['saved_events'] = profile.saved_events.all()
        return context


class AccountUpdateView(views.UpdateView):
    queryset = LibraryProfile.objects.all()
    template_name = 'accounts/account_update.html'
    form_class = LibraryProfileForm

    def get_success_url(self):
        return reverse("account details", kwargs={
            "pk": self.object.pk,
        })