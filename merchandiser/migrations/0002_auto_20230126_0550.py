# Generated by Django 3.1.13 on 2023-01-26 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandiser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandiser',
            name='img',
            field=models.ImageField(upload_to='media/merchandiser'),
        ),
    ]
