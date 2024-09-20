from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from library.lb_accounts.managers import LibraryUserManager


class LibraryUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    LIBRARY_CARD_NUMBER_LENGTH = 15

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )

    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    library_card_number = models.CharField(
        max_length=LIBRARY_CARD_NUMBER_LENGTH,
        unique=True,
        null=True,
        blank=True,
    )

    USERNAME_FIELD = 'email'

    objects = LibraryUserManager()


class LibraryProfile(models.Model):
    MAX_NAME_LENGTH = 20
    MAX_ADDRESS_LENGTH = 255
    MAX_PHONE_NUMBER_LENGTH = 20
    MAX_CITY_NAME_LENGTH = 20

    email = models.EmailField(
        max_length=30,
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    address = models.CharField(
        max_length=MAX_ADDRESS_LENGTH,
        null=False,
        blank=False,
    )

    phone_number = models.CharField(
        max_length=MAX_PHONE_NUMBER_LENGTH,
        null=False,
        blank=False,
    )

    city = models.CharField(
        max_length=MAX_CITY_NAME_LENGTH,
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        LibraryUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
