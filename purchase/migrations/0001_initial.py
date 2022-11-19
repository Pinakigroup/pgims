# Generated by Django 4.1.2 on 2022-11-16 11:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('supplier', '0001_initial'),
        ('merchandiser', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_qty', models.PositiveIntegerField(default=1)),
                ('style_detail', models.TextField()),
                ('color', models.CharField(blank=True, max_length=64, null=True)),
                ('po_date', models.DateField(default=django.utils.timezone.now)),
                ('atten', models.CharField(blank=True, max_length=64, null=True)),
                ('file_no', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('uom', models.CharField(choices=[('', 'Select'), ('kg', 'kg'), ('miter', 'miter'), ('yard', 'yard'), ('pcs', 'pcs'), ('pound', 'pound'), ('g', 'g'), ('gg', 'gg'), ('litre', 'litre'), ('dg', 'dg'), ('1000 pcs', '1000 pcs')], max_length=64, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('merchandiser_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchandiser.merchandiser')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('supplier_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier')),
            ],
        ),
    ]