# Generated by Django 5.1.3 on 2024-11-27 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='Product',
        ),
    ]