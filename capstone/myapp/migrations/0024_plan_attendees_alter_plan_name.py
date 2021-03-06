# Generated by Django 4.0.2 on 2022-05-03 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_plan_time_alter_plan_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='attendees',
            field=models.ManyToManyField(blank=True, to='myapp.Profile'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(choices=[('La Salles', 'La Salles'), ('Fresh Twisted Cafe', 'Fresh Twisted Cafe'), ('Momona', 'Momona'), ('B Street Public House', 'B Street Public House'), ('Parkside Tap House', 'Parkside Tap House'), ('The Allies Pub', 'The Allies Pub'), ('The Banshee', 'The Banshee'), ('Taps Bar and Grill', 'Taps Bar and Grill'), ('Ali Baba', 'Ali Baba'), ('Sicilian Cafe', 'Sicilian Cafe'), ('Burban Kitchen', 'Burban Kitchen'), ('Burgers and Brew', 'Burgers and Brew'), ('The Handle Bar', 'The Handle Bar'), ('Sierra Nevada Taproom & Restaurant', 'Sierra Nevada Taproom & Restaurant'), ("Spiteri's Delicatessen", "Spiteri's Delicatessen"), ('Tres Hombres Long Bar and Grill', 'Tres Hombres Long Bar and Grill'), ('Ojiya Japanese Steakhouse and Sushi Bar', 'Ojiya Japanese Steakhouse and Sushi Bar'), ("Mom's Restaurant", "Mom's Restaurant"), ('Broadway Heights', 'Broadway Heights'), ('Red Tavern', 'Red Tavern')], max_length=240),
        ),
    ]
