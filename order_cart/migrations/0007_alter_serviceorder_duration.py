# Generated by Django 5.0.1 on 2024-02-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_cart', '0006_rename_duration_minutes_servicecartitem_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceorder',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='مدة الخدمة (بالدقائق)'),
        ),
    ]
