# Generated by Django 5.0.1 on 2024-01-30 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categroy', '0001_initial'),
        ('provider_details', '0011_storestory_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='storespecialist',
            name='phone',
            field=models.CharField(default=1, max_length=9, verbose_name='رقم الهاتف'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SpecialistWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categroy.mainservice')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider_details.storespecialist')),
            ],
        ),
    ]