# Generated by Django 5.0.4 on 2024-04-20 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onepiece', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipage',
            old_name='bateau',
            new_name='nombateau',
        ),
    ]
