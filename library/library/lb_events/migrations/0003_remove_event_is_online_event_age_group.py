# Generated by Django 5.1.1 on 2024-09-28 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lb_events', '0002_remove_event_max_attendees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='is_online',
        ),
        migrations.AddField(
            model_name='event',
            name='age_group',
            field=models.TextField(default=1, verbose_name='Age Group'),
            preserve_default=False,
        ),
    ]
