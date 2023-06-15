# Generated by Django 3.2.10 on 2023-06-15 06:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
        ('store_receiver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccesRequisitionBill',
            fields=[
                ('billno', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('order_no', models.CharField(blank=True, max_length=32, null=True)),
                ('style_no', models.CharField(blank=True, max_length=32, null=True)),
                ('file_no', models.CharField(max_length=64, null=True, unique=True)),
                ('line_no', models.CharField(blank=True, max_length=32, null=True)),
                ('card_no', models.CharField(blank=True, max_length=32, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('supply_qty', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('store_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_receiver.storereceiver')),
            ],
        ),
        migrations.CreateModel(
            name='AccesRequisitionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('uom', models.CharField(choices=[('', 'Select'), ('kg', 'kg'), ('miter', 'miter'), ('yard', 'yard'), ('pcs', 'pcs'), ('pound', 'pound'), ('cone', 'cone'), ('g', 'g'), ('gg', 'gg'), ('litre', 'litre'), ('dg', 'dg'), ('1000 pcs', '1000 pcs')], max_length=64, null=True)),
                ('acces_color', models.CharField(blank=True, max_length=64, null=True)),
                ('size', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ar_billno', to='acces_requisition.accesrequisitionbill')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ar_item', to='stock.stock')),
            ],
        ),
        migrations.CreateModel(
            name='AccesRequisitionBillDetails',
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
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ar_detailsbillno', to='acces_requisition.accesrequisitionbill')),
            ],
        ),
    ]
