# Generated by Django 5.0.1 on 2024-02-15 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_cart', '0005_alter_servicecartitem_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicecartitem',
            old_name='duration_minutes',
            new_name='duration',
        ),
    ]