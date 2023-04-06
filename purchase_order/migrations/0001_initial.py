# Generated by Django 4.1.7 on 2023-04-06 06:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
        ('merchandiser', '0001_initial'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseBill',
            fields=[
                ('billno', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now=True)),
                ('buyer_name', models.CharField(max_length=64, null=True)),
                ('work_order', models.CharField(blank=True, max_length=32, null=True)),
                ('po_date', models.DateField(default=django.utils.timezone.now)),
                ('po_no', models.CharField(max_length=32, null=True)),
                ('file_no', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('detail', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('merchandiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merchandisersname', to='merchandiser.merchandiser')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliersname', to='supplier.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('unit_price', models.IntegerField(default=1)),
                ('totalprice', models.IntegerField(default=1)),
                ('uom', models.CharField(blank=True, choices=[('', 'Select'), ('kg', 'kg'), ('miter', 'miter'), ('yard', 'yard'), ('pcs', 'pcs'), ('pound', 'pound'), ('g', 'g'), ('gg', 'gg'), ('litre', 'litre'), ('dg', 'dg'), ('1000 pcs', '1000 pcs')], max_length=64, null=True)),
                ('size', models.CharField(blank=True, max_length=64, null=True)),
                ('style_no', models.CharField(blank=True, max_length=64, null=True)),
                ('color', models.CharField(blank=True, max_length=64, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchasebillno', to='purchase_order.purchasebill')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchaseitem', to='stock.stock')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseBillDetails',
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
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchasedetailsbillno', to='purchase_order.purchasebill')),
            ],
        ),
    ]
