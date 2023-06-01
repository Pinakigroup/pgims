# Generated by Django 3.2.10 on 2023-05-31 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('country', models.CharField(blank=True, max_length=64, null=True)),
                ('type', models.CharField(choices=[('', 'Select'), ('derect_customer', 'Derect Customer'), ('buying_house', 'Buying House')], max_length=64, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]