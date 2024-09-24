from django.db import models
from django.template.defaultfilters import slugify

from library.core.validators import MaxFileSizeValidator


class Author(models.Model):
    MAX_NAME_LENGTH = 50

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Item(models.Model):
    class ItemTypeChoices(models.TextChoices):
        BOOK = 'Book'
        MEDIA = 'Media'

    MAX_TITLE_LENGTH = 255
    MAX_ITEM_TYPE_LENGTH = max(len(x) for x in ItemTypeChoices)
    MAX_ISBN_LENGTH = 13

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='items_author'
    )

    genre = models.CharField(
        max_length=100,
    )

    item_type = models.CharField(
        max_length=MAX_ITEM_TYPE_LENGTH,
        choices=ItemTypeChoices.choices
    )

    publication_date = models.DateField()

    isbn = models.CharField(
        max_length=MAX_ISBN_LENGTH,
        unique=True
    )

    available_copies = models.PositiveIntegerField(
        default=1
    )

    total_copies = models.PositiveIntegerField(
        default=1
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    item_image = models.ImageField(
        upload_to='item_images/',
        blank=True,
        null=True,
        validators=[MaxFileSizeValidator(10 * 1024 * 1024)],
    )

    def save(self, *args, **kwargs):
        date_str = self.publication_date.strftime('%Y-%B-%d')
        slug_base = f"{self.item_type}-{date_str}-{self.author}-{self.title}-{self.genre}"
        self.slug = slugify(slug_base)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
