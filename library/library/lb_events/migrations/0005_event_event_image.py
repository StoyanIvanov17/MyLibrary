# Generated by Django 5.1.1 on 2024-09-28 22:53

import library.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lb_events', '0004_alter_event_age_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_image',
            field=models.ImageField(default=2, upload_to='event_images/', validators=[library.core.validators.MaxFileSizeValidator(10485760)]),
            preserve_default=False,
        ),
    ]