# Generated by Django 3.2.10 on 2023-06-20 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acces_requisition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesrequisitionbill',
            name='file_no',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
