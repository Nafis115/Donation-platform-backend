# Generated by Django 5.0.6 on 2024-08-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='managermodel',
            name='designation',
            field=models.CharField(default='manager', max_length=100),
        ),
    ]
