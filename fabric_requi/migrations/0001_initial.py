# Generated by Django 3.2.10 on 2023-07-24 09:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store_receiver', '0001_initial'),
        ('store', '0001_initial'),
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
                ('fileno_po', models.CharField(max_length=64, null=True)),
                ('order_no', models.CharField(blank=True, max_length=32, null=True)),
                ('card_no', models.CharField(blank=True, max_length=32, null=True)),
                ('floor', models.CharField(choices=[('', 'Select'), ('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th')], max_length=64, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('store_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_receiver.storereceiver')),
                ('work_order_fr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fabric_work_order', to='store.storebill')),
            ],
        ),
        migrations.CreateModel(
            name='FabricRequisitionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('uom', models.CharField(choices=[('', 'Select'), ('kg', 'kg'), ('miter', 'miter'), ('yard', 'yard'), ('pcs', 'pcs'), ('pound', 'pound'), ('g', 'g'), ('gg', 'gg'), ('litre', 'litre'), ('dz', 'dz'), ('1000 pcs', '1000 pcs')], max_length=64, null=True)),
                ('unit', models.CharField(choices=[('', 'Select'), ('miter', 'miter'), ('yard', 'yard')], max_length=64, null=True)),
                ('style_no', models.CharField(blank=True, max_length=64, null=True)),
                ('fab_color', models.CharField(blank=True, max_length=64, null=True)),
                ('order_qty', models.IntegerField(blank=True, default=0, null=True)),
                ('cutting_qty', models.IntegerField(blank=True, default=0, null=True)),
                ('cad_consumption', models.CharField(blank=True, max_length=64, null=True)),
                ('requard_qty', models.IntegerField(blank=True, default=0, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_billno', to='fabric_requi.fabricrequisitionbill')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_item', to='stock.stock')),
            ],
        ),
        migrations.CreateModel(
            name='FabricRequisitionBillDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_detailsbillno', to='fabric_requi.fabricrequisitionbill')),
            ],
        ),
    ]
