# Generated by Django 5.0.6 on 2024-08-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0003_campaigns_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigns',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
