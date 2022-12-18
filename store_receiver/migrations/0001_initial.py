# Generated by Django 3.1.13 on 2022-12-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreReceiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('designation', models.CharField(blank=True, max_length=64, null=True)),
                ('email', models.EmailField(blank=True, max_length=64, unique=True)),
                ('phone', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]