# Generated by Django 5.1.1 on 2024-09-18 21:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('is_online', models.BooleanField(default=False)),
                ('max_attendees', models.PositiveIntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rsvp_date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='rsvps_event', to='lb_events.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
