# Generated by Django 3.2.10 on 2023-09-06 07:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=64, null=True)),
                ('master_lc_sc', models.CharField(blank=True, max_length=128, null=True)),
                ('abc', models.CharField(max_length=50)),
                ('xyz', models.CharField(blank=True, choices=[('', 'Select'), ('30 day', '30 day'), ('45 day', '45 day'), ('60 day', '60 day'), ('75 day', '75 day'), ('90 day', '90 day'), ('105 day', '105 day'), ('120 day', '120 day')], max_length=64, null=True)),
                ('exp_date_of_delivery', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('buyer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyersname', to='buyer.buyer')),
            ],
        ),
    ]
