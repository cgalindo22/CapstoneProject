# Generated by Django 4.0.2 on 2022-05-05 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0032_alter_plan_name_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(choices=[('La Salles', 'La Salles'), ('Fresh Twisted Cafe', 'Fresh Twisted Cafe'), ('The Banshee', 'The Banshee'), ('Momona', 'Momona'), ('B Street Public House', 'B Street Public House'), ('Parkside Tap House', 'Parkside Tap House'), ('Sicilian Cafe', 'Sicilian Cafe'), ('The Allies Pub', 'The Allies Pub'), ('Taps Bar and Grill', 'Taps Bar and Grill'), ('Tres Hombres Long Bar and Grill', 'Tres Hombres Long Bar and Grill'), ('Burban Kitchen', 'Burban Kitchen'), ('Ali Baba', 'Ali Baba'), ('Burgers and Brew', 'Burgers and Brew'), ('The Handle Bar', 'The Handle Bar'), ('Sierra Nevada Taproom & Restaurant', 'Sierra Nevada Taproom & Restaurant'), ("Spiteri's Delicatessen", "Spiteri's Delicatessen"), ('Red Tavern', 'Red Tavern'), ('Ojiya Japanese Steakhouse and Sushi Bar', 'Ojiya Japanese Steakhouse and Sushi Bar'), ("Mom's Restaurant", "Mom's Restaurant"), ('Broadway Heights', 'Broadway Heights')], max_length=240),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
