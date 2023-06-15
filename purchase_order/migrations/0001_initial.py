# Generated by Django 3.2.10 on 2023-06-15 06:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import purchase_order.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
        ('supplier', '0001_initial'),
        ('file', '0001_initial'),
        ('merchandiser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseBill',
            fields=[
                ('billno', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now=True)),
                ('buyer_name', models.CharField(max_length=64, null=True)),
                ('po_no', models.CharField(blank=True, max_length=32, null=True)),
                ('style_no', models.CharField(blank=True, max_length=32, null=True)),
                ('work_order', models.CharField(default=purchase_order.models.generate_random_number, max_length=64)),
                ('wo_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('sale_contact', models.CharField(blank=True, max_length=64, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fileno_po', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fileno_pos', to='file.file')),
                ('merchandiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merchandisersname', to='merchandiser.merchandiser')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliersname', to='supplier.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('unit_price', models.IntegerField(blank=True, default=1, null=True)),
                ('totalprice', models.IntegerField(blank=True, default=1, null=True)),
                ('uom', models.CharField(blank=True, choices=[('', 'Select'), ('kg', 'kg'), ('miter', 'miter'), ('yard', 'yard'), ('pcs', 'pcs'), ('pound', 'pound'), ('g', 'g'), ('gg', 'gg'), ('litre', 'litre'), ('dg', 'dg'), ('1000 pcs', '1000 pcs')], max_length=64, null=True)),
                ('size', models.CharField(blank=True, max_length=64, null=True)),
                ('style', models.CharField(blank=True, max_length=64, null=True)),
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
