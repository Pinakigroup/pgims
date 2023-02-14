# Generated by Django 4.1.6 on 2023-02-14 09:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store_receiver', '0001_initial'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccesRequisitionBill',
            fields=[
                ('billno', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('order_no', models.CharField(blank=True, max_length=32, null=True)),
                ('style_no', models.CharField(blank=True, max_length=32, null=True)),
                ('line_no', models.CharField(blank=True, max_length=32, null=True)),
                ('card_no', models.CharField(blank=True, max_length=32, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('supply_qty', models.PositiveIntegerField(default=1)),
                ('remarks', models.TextField()),
                ('sr_designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_receiver.storereceiver')),
            ],
        ),
        migrations.CreateModel(
            name='AccesRequisitionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('unit_price', models.IntegerField(default=1)),
                ('totalprice', models.IntegerField(default=1)),
                ('uom', models.CharField(choices=[('', 'Select'), ('kg', 'kg'), ('miter', 'miter'), ('yard', 'yard'), ('pcs', 'pcs'), ('pound', 'pound'), ('g', 'g'), ('gg', 'gg'), ('litre', 'litre'), ('dg', 'dg'), ('1000 pcs', '1000 pcs')], max_length=64, null=True)),
                ('acces_color', models.CharField(blank=True, max_length=64, null=True)),
                ('size', models.CharField(blank=True, max_length=64, null=True, unique=True)),
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
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ar_detailsbillno', to='acces_requisition.accesrequisitionbill')),
            ],
        ),
    ]
