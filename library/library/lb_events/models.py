from django.db import models
from django.utils.text import slugify

from library.lb_accounts.models import LibraryUser


from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Event(models.Model):
    name = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    date = models.DateTimeField()

    location = models.CharField(
        max_length=255
    )

    is_online = models.BooleanField(
        default=False
    )

    max_attendees = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        date_str = self.date.strftime('%Y-%B-%d')
        slug_base = f"{self.name}-{date_str}-{self.location}"
        self.slug = slugify(slug_base)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class RSVP(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.RESTRICT,
        related_name='rsvps_event'
    )

    rsvp_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.user} - {self.event}'
