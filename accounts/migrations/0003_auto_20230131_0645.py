# Generated by Django 3.1.13 on 2023-01-31 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230130_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='user_acc',
        ),
    ]