# Generated by Django 4.0.2 on 2022-05-03 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_profile_first_name_profile_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
