# Generated by Django 4.2.6 on 2023-12-28 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provider_details', '0008_followingstore'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/provider/store/', verbose_name='رفع الصورة')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='story_of_store', to='provider_details.store', verbose_name='المتجر التابع له')),
            ],
            options={
                'unique_together': {('store', 'image')},
            },
        ),
    ]