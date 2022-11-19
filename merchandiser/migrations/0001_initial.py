# Generated by Django 4.1.2 on 2022-11-16 10:08

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
                ('joining_date', models.DateField(default=django.utils.timezone.now)),
                ('email', models.EmailField(blank=True, max_length=64, unique=True)),
                ('phone', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('access_area', models.CharField(blank=True, max_length=64)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]