# Generated by Django 4.2.6 on 2023-12-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider_details', '0003_service_main_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='hours_Service',
            field=models.TimeField(blank=True, null=True, verbose_name='ساعات الخدمة'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='اسم المنتج'),
        ),
    ]