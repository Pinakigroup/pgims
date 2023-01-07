# Generated by Django 3.1.13 on 2023-01-07 06:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FabricRequisitionBill',
            fields=[
                ('billno', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('buyer_name', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('po_no', models.CharField(blank=True, max_length=32, null=True)),
                ('order_no', models.CharField(blank=True, max_length=32, null=True)),
                ('card_no', models.CharField(blank=True, max_length=32, null=True)),
                ('floor', models.CharField(choices=[('', 'Select'), ('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th')], max_length=64, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('fabric_detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FabricRequisitionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('unit_price', models.IntegerField(default=1)),
                ('totalprice', models.IntegerField(default=1)),
                ('uom', models.CharField(choices=[('', 'Select'), ('kg', 'kg'), ('miter', 'miter'), ('yard', 'yard'), ('pcs', 'pcs'), ('pound', 'pound'), ('g', 'g'), ('gg', 'gg'), ('litre', 'litre'), ('dg', 'dg'), ('1000 pcs', '1000 pcs')], max_length=64, null=True)),
                ('style_no', models.CharField(blank=True, max_length=64, null=True)),
                ('fab_color', models.CharField(blank=True, max_length=64, null=True)),
                ('order_qty', models.IntegerField(default=0)),
                ('cutting_qty', models.IntegerField(default=0)),
                ('consumption', models.IntegerField(default=0)),
                ('requard_qty', models.IntegerField(default=0)),
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_billno', to='fabric_requi.fabricrequisitionbill')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_item', to='stock.stock')),
            ],
        ),
        migrations.CreateModel(
            name='FabricRequisitionBillDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eway', models.CharField(blank=True, max_length=50, null=True)),
                ('veh', models.CharField(blank=True, max_length=50, null=True)),
                ('destination', models.CharField(blank=True, max_length=50, null=True)),
                ('po', models.CharField(blank=True, max_length=50, null=True)),
                ('cgst', models.CharField(blank=True, max_length=50, null=True)),
                ('sgst', models.CharField(blank=True, max_length=50, null=True)),
                ('igst', models.CharField(blank=True, max_length=50, null=True)),
                ('cess', models.CharField(blank=True, max_length=50, null=True)),
                ('tcs', models.CharField(blank=True, max_length=50, null=True)),
                ('total', models.CharField(blank=True, max_length=50, null=True)),
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_detailsbillno', to='fabric_requi.fabricrequisitionbill')),
            ],
        ),
    ]
