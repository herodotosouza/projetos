# Generated by Django 3.2 on 2021-04-28 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_pet_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='veterinario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=11, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('begin_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='pet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'veterinario',
            },
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=11, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('begin_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='pet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
    ]
