# Generated by Django 3.1.13 on 2022-12-10 06:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.CharField(choices=[('', 'Select'), ('Invoice', 'Invoice'), ('DC', 'DC')], max_length=64, null=True)),
                ('report_no', models.CharField(max_length=64, null=True)),
                ('report_date', models.DateField(default=django.utils.timezone.now)),
                ('file_no', models.CharField(max_length=64, null=True)),
                ('lc', models.CharField(max_length=64, null=True)),
                ('rec_qty', models.PositiveIntegerField(default=1)),
                ('uom', models.CharField(choices=[('', 'Select'), ('kg', 'kg'), ('miter', 'miter'), ('yard', 'yard'), ('pcs', 'pcs'), ('pound', 'pound'), ('g', 'g'), ('gg', 'gg'), ('litre', 'litre'), ('dg', 'dg'), ('1000 pcs', '1000 pcs')], max_length=64, null=True)),
                ('unit_price', models.FloatField()),
                ('total_price', models.FloatField(default=0, editable=False)),
                ('due_qty', models.PositiveIntegerField(default=0, editable=False)),
                ('buyer_name', models.CharField(max_length=64, null=True)),
                ('style_no', models.CharField(blank=True, max_length=32, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier')),
                ('product_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
