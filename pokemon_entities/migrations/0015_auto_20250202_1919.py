# Generated by Django 3.1.14 on 2025-02-02 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_auto_20250201_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='lisappeared_at',
            new_name='disappeared_at',
        ),
    ]
