# Generated by Django 5.0.1 on 2024-06-06 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_login', '0023_alter_myuser_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pendingclient',
            name='password',
        ),
        migrations.CreateModel(
            name='PendingProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('otp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pendingProvider', to='auth_login.otprequest')),
            ],
        ),
    ]