# Generated by Django 5.0.6 on 2024-08-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0004_alter_donation_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
