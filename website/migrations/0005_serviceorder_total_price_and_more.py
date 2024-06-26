# Generated by Django 5.0.4 on 2024-04-26 06:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_roombooking_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorder',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='serviceorder',
            name='order_date',
            field=models.DateField(verbose_name=django.utils.timezone.now),
        ),
    ]
