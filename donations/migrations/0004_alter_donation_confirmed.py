# Generated by Django 5.0.6 on 2024-08-22 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_donation_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='confirmed',
            field=models.CharField(choices=[('confirm', 'Confirm'), ('pending', 'Pending')], default='pending', max_length=20),
        ),
    ]
