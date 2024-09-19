from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class LibraryCardOrEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(library_card_number=username)
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(email=username)
            except UserModel.DoesNotExist:
                return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None


class AdminEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Admin uses email to log in
        if '@' in username:
            try:
                user = UserModel.objects.get(email=username)
                if user.check_password(password) and user.is_staff:
                    return user
            except UserModel.DoesNotExist:
                return None
        return None
