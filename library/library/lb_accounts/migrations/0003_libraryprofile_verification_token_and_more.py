# Generated by Django 5.1.1 on 2024-10-21 19:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lb_accounts', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryprofile',
            name='verification_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='libraryprofile',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
