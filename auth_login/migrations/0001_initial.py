# Generated by Django 4.2.6 on 2023-12-09 14:13

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('categroy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=255, verbose_name='الاسم الكامل')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='البريد الإلكتروني')),
                ('phone', models.CharField(max_length=9, verbose_name='رقم الهاتف')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='نشاط الحساب')),
                ('is_staff', models.BooleanField(blank=True, default=False, verbose_name='دخول لوحة التحكم')),
                ('is_superuser', models.BooleanField(blank=True, default=False, verbose_name='سوبر أدمن')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الإنشاء')),
                ('updated_on', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ التحديث')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True, verbose_name='خط العرض')),
                ('longitude', models.CharField(blank=True, max_length=255, null=True, verbose_name='خط الطول')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='نص العنوان')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth_login.myuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True, verbose_name='خط العرض')),
                ('longitude', models.CharField(blank=True, max_length=255, null=True, verbose_name='خط الطول')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='نص العنوان')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categroy.category', verbose_name='التصنيف التابع له')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth_login.myuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
