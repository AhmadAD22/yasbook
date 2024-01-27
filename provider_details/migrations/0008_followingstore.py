# Generated by Django 4.2.6 on 2023-12-28 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_login', '0001_initial'),
        ('provider_details', '0007_alter_storeadminservices_main_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowingStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_login.customer', verbose_name='الزبون')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider_details.store', verbose_name='المتجر التابع له')),
            ],
            options={
                'unique_together': {('store', 'customer')},
            },
        ),
    ]