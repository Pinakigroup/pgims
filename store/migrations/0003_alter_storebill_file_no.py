# Generated by Django 4.1.7 on 2023-02-23 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_storebill_img_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storebill',
            name='file_no',
            field=models.CharField(max_length=64, null=True),
        ),
    ]