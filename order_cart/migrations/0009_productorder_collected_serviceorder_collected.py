# Generated by Django 5.0.1 on 2024-02-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_cart', '0008_productorder_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='collected',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='تم تحصيلها'),
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='collected',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='تم تحصيلها'),
        ),
    ]