# Generated by Django 3.2.10 on 2023-09-09 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_storebill_received_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storebill',
            name='received_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]