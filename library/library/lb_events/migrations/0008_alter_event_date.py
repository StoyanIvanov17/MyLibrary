# Generated by Django 5.1.1 on 2024-09-28 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lb_events', '0007_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
    ]
