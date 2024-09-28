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

    age_group = models.TextField(
        verbose_name='Age Group'
    )

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        date_str = self.date.strftime('%Y-%B-%d')
        slug_base = f"{self.name}-{date_str}-{self.location}-{self.age_group}"
        self.slug = slugify(slug_base)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
