# Generated by Django 4.2.6 on 2023-11-05 11:38

from django.db import migrations, models
import purchase_order.models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0002_alter_purchasebill_work_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasebill',
            name='work_order',
            field=models.CharField(default=purchase_order.models.generate_random_number, max_length=64),
        ),
    ]
