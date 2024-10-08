# Generated by Django 5.1.1 on 2024-10-08 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lb_accounts', '0001_initial'),
        ('lb_collections', '0004_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb_accounts.libraryprofile'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb_accounts.libraryprofile'),
        ),
    ]
