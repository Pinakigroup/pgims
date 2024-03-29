# Generated by Django 4.2.6 on 2023-11-21 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('remarks', '0001_initial'),
        ('stock', '0001_initial'),
        ('store', '0001_initial'),
        ('unit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FabricRequisitionBill',
            fields=[
                ('billno', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('buyer_name', models.CharField(blank=True, max_length=64, null=True)),
                ('fileno_po', models.CharField(max_length=64, null=True)),
                ('po_no', models.CharField(blank=True, max_length=32, null=True)),
                ('style_no', models.CharField(blank=True, max_length=32, null=True)),
                ('card_no', models.CharField(blank=True, max_length=32, null=True)),
                ('unit', models.CharField(choices=[('', 'Select'), ('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd')], max_length=64, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remarksname_fabric', to='remarks.remarks')),
                ('work_order_fr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fabric_work_order', to='store.storebill')),
            ],
        ),
        migrations.CreateModel(
            name='FabricRequisitionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=9)),
                ('balance_quantity', models.DecimalField(decimal_places=2, max_digits=9)),
                ('style', models.CharField(blank=True, max_length=64, null=True)),
                ('color', models.CharField(blank=True, max_length=64, null=True)),
                ('order_qty', models.DecimalField(decimal_places=2, max_digits=9)),
                ('cutting_qty', models.DecimalField(decimal_places=2, max_digits=9)),
                ('cad_consumption', models.DecimalField(decimal_places=2, max_digits=9)),
                ('requard_qty', models.DecimalField(decimal_places=2, max_digits=9)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_billno', to='fabric_requi.fabricrequisitionbill')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_item', to='stock.stock')),
                ('uom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uom_of_fabric_issue', to='unit.unit')),
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
