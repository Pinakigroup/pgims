# Generated by Django 3.2.10 on 2023-06-20 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabric_requi', '0002_auto_20230618_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabricrequisitionbill',
            name='wo_no',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
