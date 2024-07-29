# Generated by Django 5.0.1 on 2024-07-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categroy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='media/category/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]