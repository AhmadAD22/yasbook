# Generated by Django 5.0.1 on 2024-02-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_login', '0004_alter_providersubscription_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providersubscription',
            name='profit_ratio',
            field=models.IntegerField(default=0, verbose_name='Profit Ratio'),
        ),
    ]
