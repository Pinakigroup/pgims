# Generated by Django 4.2.6 on 2023-11-19 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acces_requisition', '0003_rename_acces_color_accesrequisitionitem_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesrequisitionbill',
            name='order_no',
        ),
    ]
