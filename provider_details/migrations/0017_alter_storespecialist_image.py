# Generated by Django 5.0.1 on 2024-02-02 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider_details', '0016_storespecialist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storespecialist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/provider/specialists/', verbose_name='رفع الصورة'),
        ),
    ]
