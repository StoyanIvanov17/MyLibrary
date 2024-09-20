
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class LibraryUserCreationForm(auth_forms.UserCreationForm):
    usable_password = None
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', )


class LibraryChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
