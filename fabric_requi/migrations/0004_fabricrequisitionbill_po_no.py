# Generated by Django 4.2.6 on 2023-11-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabric_requi', '0003_rename_order_no_fabricrequisitionbill_style_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabricrequisitionbill',
            name='po_no',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
