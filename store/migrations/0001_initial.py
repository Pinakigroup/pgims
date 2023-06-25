# Generated by Django 3.2.10 on 2023-06-25 04:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store_receiver', '0001_initial'),
        ('purchase_order', '0001_initial'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreBill',
            fields=[
                ('billno', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now=True)),
                ('supplier', models.CharField(max_length=64, null=True)),
                ('buyer_name', models.CharField(max_length=64, null=True)),
                ('report', models.CharField(choices=[('', 'Select'), ('Invoice', 'Invoice'), ('DC', 'DC')], max_length=64, null=True)),
                ('report_no', models.CharField(blank=True, max_length=64, null=True)),
                ('report_date', models.DateField(default=django.utils.timezone.now)),
                ('pi_no', models.CharField(blank=True, max_length=150, null=True)),
                ('received_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('img_file', models.ImageField(blank=True, default='blank.png', null=True, upload_to='store')),
                ('work_order', models.CharField(max_length=64, null=True)),
                ('master_lc_sc', models.CharField(max_length=64, null=True)),
                ('style_no', models.CharField(blank=True, max_length=32, null=True)),
                ('lot_no', models.CharField(blank=True, max_length=64, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('store_location', models.CharField(blank=True, max_length=64, null=True)),
                ('order_qty', models.IntegerField(blank=True, default=0, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file_no_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_file_no', to='purchase_order.purchasebill')),
                ('received_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_receivers', to='store_receiver.storereceiver')),
            ],
        ),
        migrations.CreateModel(
            name='StoreItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('fabric_color', models.CharField(blank=True, max_length=64, null=True)),
                ('uom', models.CharField(choices=[('', 'Select'), ('kg', 'kg'), ('miter', 'miter'), ('yard', 'yard'), ('pcs', 'pcs'), ('pound', 'pound'), ('g', 'g'), ('gg', 'gg'), ('litre', 'litre'), ('dg', 'dg'), ('1000 pcs', '1000 pcs')], max_length=64, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storebillno', to='store.storebill')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storeitem', to='stock.stock')),
            ],
        ),
        migrations.CreateModel(
            name='StoreBillDetails',
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
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storedetailsbillno', to='store.storebill')),
            ],
        ),
    ]
