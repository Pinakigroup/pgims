# Generated by Django 4.1.7 on 2023-04-12 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acces_requisition', '0004_rename_supervisor_accesrequisitionbill_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accesrequisitionbill',
            old_name='sr_designation',
            new_name='store_receiver',
        ),
    ]
