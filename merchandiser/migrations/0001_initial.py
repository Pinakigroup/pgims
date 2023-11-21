# Generated by Django 4.2.6 on 2023-11-21 05:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchandiser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_id', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('designation', models.CharField(blank=True, max_length=64, null=True)),
                ('joining_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('email', models.EmailField(blank=True, max_length=64, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('access_area', models.CharField(blank=True, max_length=64, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='merchandiser')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
