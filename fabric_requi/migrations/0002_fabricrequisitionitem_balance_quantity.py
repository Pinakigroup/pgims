# Generated by Django 3.2.10 on 2023-08-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabric_requi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabricrequisitionitem',
            name='balance_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
