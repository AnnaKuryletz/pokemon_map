# Generated by Django 3.1.14 on 2025-02-01 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_auto_20250201_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Appeared_at',
            new_name='appeared_at',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Defence',
            new_name='defence',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Health',
            new_name='health',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Lat',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Level',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Disappeared_at',
            new_name='lisappeared_at',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Lon',
            new_name='lon',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Stamina',
            new_name='stamina',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Strength',
            new_name='strength',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.pokemon', verbose_name='Предыдущая эволюция покемона'),
        ),
    ]
