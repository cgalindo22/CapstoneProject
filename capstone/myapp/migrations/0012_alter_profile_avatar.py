# Generated by Django 4.0.2 on 2022-04-01 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_profile_avatar_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='static/images/defalut_profile.jpeg', upload_to='profile/'),
        ),
    ]