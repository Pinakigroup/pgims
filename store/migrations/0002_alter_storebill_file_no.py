# Generated by Django 3.2.10 on 2023-05-31 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storebill',
            name='file_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase_order.purchasebill'),
        ),
    ]
