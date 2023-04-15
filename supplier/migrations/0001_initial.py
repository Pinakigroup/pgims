# Generated by Django 4.1.6 on 2023-04-15 07:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('supplier_name', models.CharField(max_length=64, null=True)),
                ('company_name', models.CharField(max_length=64, null=True)),
                ('office_address', models.CharField(max_length=64, null=True)),
                ('office_postal_code', models.IntegerField(blank=True)),
                ('office_country', models.CharField(blank=True, max_length=64, null=True)),
                ('office_tphone', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('factory_address', models.CharField(blank=True, max_length=64, null=True)),
                ('factory_postal_code', models.IntegerField(blank=True)),
                ('factory_country', models.CharField(blank=True, max_length=64, null=True)),
                ('factory_tphone', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('vat_identi_no', models.CharField(blank=True, max_length=32)),
                ('expiry_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('trade_license_no', models.CharField(blank=True, max_length=32)),
                ('owner_name', models.CharField(blank=True, max_length=64, null=True)),
                ('owner_phone', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('owner_email', models.EmailField(blank=True, max_length=64, unique=True)),
                ('first_cp_name', models.CharField(blank=True, max_length=64, null=True)),
                ('first_cp_position', models.CharField(blank=True, max_length=64, null=True)),
                ('first_cp_phone', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('first_cp_email', models.EmailField(blank=True, max_length=64, unique=True)),
                ('sec_cp_name', models.CharField(blank=True, max_length=64, null=True)),
                ('sec_cp_position', models.CharField(blank=True, max_length=64, null=True)),
                ('sec_cp_phone', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('sec_cp_email', models.EmailField(blank=True, max_length=64, unique=True)),
                ('account_name', models.CharField(max_length=64, null=True)),
                ('account_no', models.CharField(max_length=32, null=True)),
                ('bank_name', models.CharField(max_length=64, null=True)),
                ('bank_address', models.CharField(max_length=64, null=True)),
                ('swift', models.CharField(max_length=64, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
