# Generated by Django 5.0.1 on 2024-04-19 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_login', '0018_promotionsubscription_image_delete_promotion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='البريد الإلكتروني'),
        ),
        migrations.AlterField(
            model_name='promotionsubscription',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/provider/', verbose_name='رفع الصورة'),
        ),
    ]
