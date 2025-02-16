# Generated by Django 5.0.8 on 2025-02-02 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trajectories', '0002_drivercardata_vehicle_address_vehicle_card_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='driver_status',
            field=models.CharField(blank=True, choices=[('ready_to_work', 'ready_to_work'), ('has_work', 'has_work'), ('processed', 'processed'), ('not_processed', 'not_processed')], default='ready_to_work', max_length=50, null=True),
        ),
    ]
