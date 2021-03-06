# Generated by Django 4.0.2 on 2022-05-04 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_remove_profile_first_name_remove_profile_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(choices=[('La Salles', 'La Salles'), ('Momona', 'Momona'), ('B Street Public House', 'B Street Public House'), ('Parkside Tap House', 'Parkside Tap House'), ('The Allies Pub', 'The Allies Pub'), ('The Banshee', 'The Banshee'), ('Taps Bar and Grill', 'Taps Bar and Grill'), ('Fresh Twisted Cafe', 'Fresh Twisted Cafe'), ('Sicilian Cafe', 'Sicilian Cafe'), ('Burban Kitchen', 'Burban Kitchen'), ('Burgers and Brew', 'Burgers and Brew'), ('The Handle Bar', 'The Handle Bar'), ('Ali Baba', 'Ali Baba'), ('Sierra Nevada Taproom & Restaurant', 'Sierra Nevada Taproom & Restaurant'), ("Spiteri's Delicatessen", "Spiteri's Delicatessen"), ('Tres Hombres Long Bar and Grill', 'Tres Hombres Long Bar and Grill'), ('Ojiya Japanese Steakhouse and Sushi Bar', 'Ojiya Japanese Steakhouse and Sushi Bar'), ("Mom's Restaurant", "Mom's Restaurant"), ('Red Tavern', 'Red Tavern'), ('5th Street Steakhouse', '5th Street Steakhouse')], max_length=240),
        ),
    ]
