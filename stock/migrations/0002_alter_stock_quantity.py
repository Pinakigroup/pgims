# Generated by Django 3.2.10 on 2023-08-22 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
