# Generated by Django 5.0.1 on 2024-04-08 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_login', '0017_promotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotionsubscription',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/provider/store/', verbose_name='رفع الصورة'),
        ),
        migrations.DeleteModel(
            name='promotion',
        ),
    ]