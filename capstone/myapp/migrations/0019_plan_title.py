# Generated by Django 4.0.2 on 2022-04-20 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_plan_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='title',
            field=models.CharField(default=1, max_length=240),
            preserve_default=False,
        ),
    ]
