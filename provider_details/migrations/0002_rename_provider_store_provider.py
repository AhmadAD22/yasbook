# Generated by Django 4.2.6 on 2023-12-09 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider_details', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='Provider',
            new_name='provider',
        ),
    ]