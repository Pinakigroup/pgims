# Generated by Django 3.2.10 on 2023-05-30 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_rename_file_no_file_file'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storebill',
            name='file_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file.file'),
        ),
    ]
