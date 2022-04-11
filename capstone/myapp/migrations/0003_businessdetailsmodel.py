# Generated by Django 4.0.2 on 2022-03-09 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_commentmodel_author_replymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessDetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hours', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=4)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]