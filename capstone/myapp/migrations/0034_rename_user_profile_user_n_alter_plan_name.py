# Generated by Django 4.0.2 on 2022-05-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_alter_plan_name_alter_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='user_n',
        ),
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(choices=[('La Salles', 'La Salles'), ('B Street Public House', 'B Street Public House'), ('Parkside Tap House', 'Parkside Tap House'), ('The Allies Pub', 'The Allies Pub'), ('Momona', 'Momona'), ('The Banshee', 'The Banshee'), ('Taps Bar and Grill', 'Taps Bar and Grill'), ('Fresh Twisted Cafe', 'Fresh Twisted Cafe'), ('Sicilian Cafe', 'Sicilian Cafe'), ('Ali Baba', 'Ali Baba'), ("Spiteri's Delicatessen", "Spiteri's Delicatessen"), ('Burban Kitchen', 'Burban Kitchen'), ('Tres Hombres Long Bar and Grill', 'Tres Hombres Long Bar and Grill'), ('Sierra Nevada Taproom & Restaurant', 'Sierra Nevada Taproom & Restaurant'), ('Burgers and Brew', 'Burgers and Brew'), ('The Handle Bar', 'The Handle Bar'), ("Mom's Restaurant", "Mom's Restaurant"), ('Ojiya Japanese Steakhouse and Sushi Bar', 'Ojiya Japanese Steakhouse and Sushi Bar'), ('Red Tavern', 'Red Tavern'), ('Main Street Pizza', 'Main Street Pizza')], max_length=240),
        ),
    ]
