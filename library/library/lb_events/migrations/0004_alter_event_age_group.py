# Generated by Django 5.1.1 on 2024-09-28 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lb_events', '0003_remove_event_is_online_event_age_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='age_group',
            field=models.CharField(max_length=50, verbose_name='Age Group'),
        ),
    ]
