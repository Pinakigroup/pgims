# Generated by Django 3.2.10 on 2023-07-31 05:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_storebill_report_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storebill',
            name='report_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
