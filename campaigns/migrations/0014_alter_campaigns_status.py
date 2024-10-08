# Generated by Django 5.0.6 on 2024-09-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0013_alter_campaigns_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaigns',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('pending', 'Pending'), ('completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]
