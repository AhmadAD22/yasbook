# Generated by Django 5.0.1 on 2024-02-22 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider_details', '0018_alter_store_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='hours_Service',
        ),
        migrations.AddField(
            model_name='service',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='مدة الخدمة (بالدقائق)'),
        ),
    ]