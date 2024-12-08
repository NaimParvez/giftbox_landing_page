# Generated by Django 5.1.3 on 2024-12-03 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_zone',
            field=models.CharField(default='Others', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
