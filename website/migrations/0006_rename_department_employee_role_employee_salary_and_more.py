# Generated by Django 5.0.4 on 2024-04-26 09:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_serviceorder_total_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='department',
            new_name='role',
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='serviceorder',
            name='order_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]