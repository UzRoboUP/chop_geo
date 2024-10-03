# Generated by Django 5.0.8 on 2024-09-28 10:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DriverCardData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('card_number', models.CharField(blank=True, max_length=16, null=True, verbose_name='Номер карты')),
            ],
            options={
                'verbose_name': 'Данные карты водителя',
                'verbose_name_plural': 'Данные карты водителя',
                'db_table': 'driver_card_data',
                'ordering': ['created_at'],
            },
        ),
    ]