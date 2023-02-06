# Generated by Django 3.1.13 on 2023-02-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='designation',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Designation'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img_profile',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True),
        ),
    ]
