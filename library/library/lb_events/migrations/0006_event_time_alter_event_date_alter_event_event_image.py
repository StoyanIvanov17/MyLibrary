# Generated by Django 5.1.1 on 2024-09-28 23:12

import library.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lb_events', '0005_event_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(upload_to='event_images/', validators=[library.core.validators.MaxFileSizeValidator(10485760)], verbose_name='Event Image'),
        ),
    ]