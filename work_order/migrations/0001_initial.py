# Generated by Django 4.2.6 on 2023-11-21 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('purchase_order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrderBill',
            fields=[
                ('billno', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now=True)),
                ('style_no', models.CharField(blank=True, max_length=32, null=True)),
                ('work_order', models.CharField(max_length=64, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('f_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wo_file_no', to='purchase_order.purchasebill')),
            ],
        ),
    ]
