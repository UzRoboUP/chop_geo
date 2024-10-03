# Generated by Django 5.0.8 on 2024-09-28 10:51

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
        ('trajectories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverCarData',
            fields=[
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('car_model', models.CharField(max_length=255, verbose_name='Модель автомобиля')),
                ('car_brand', models.CharField(max_length=255, verbose_name='Марка машины')),
                ('car_service_type', models.CharField(max_length=255, verbose_name='Тип обслуживания автомобиля')),
                ('manufactured_year', models.DateField(verbose_name='Год выпуска')),
                ('government_number', models.CharField(max_length=255, verbose_name='Государственный номер')),
                ('tech_passport_number', models.CharField(max_length=255, verbose_name='Номер технического пароля')),
                ('issue_date_of_tech_passport', models.DateField(verbose_name='Дата выдачи технического паспорта')),
                ('issue_date_of_power_attorney', models.DateField(verbose_name='Дата выдачи доверености')),
            ],
            options={
                'verbose_name': 'Данные водителя об автомобиле',
                'verbose_name_plural': 'Данные водителя об автомобиле',
                'db_table': 'driver_car_data',
                'ordering': ['created_at'],
            },
        ),
        migrations.AddField(
            model_name='vehicle',
            name='address',
            field=models.CharField(default='a', max_length=255, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='card_data',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_driver_card', to='billing.drivercarddata', verbose_name='данные карты водителя'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='driver_status',
            field=models.CharField(blank=True, choices=[('ready_to_work', 'ready_to_work'), ('has_work', 'has_work'), ('processed', 'processed'), ('not-processed', 'not-processed')], default='ready_to_work', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='full_name',
            field=models.CharField(default='Kairat Sultan', max_length=255, verbose_name='ФИО'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='guid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.URLField(blank=True, null=True, verbose_name='Фото профиля'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='last_active_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Last active time'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True, verbose_name='Дата изменения'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_data',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trajectories.drivercardata'),
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone_number', models.CharField(blank=True, max_length=50, verbose_name='Номер телефона')),
                ('first_side_passport', models.URLField(blank=True, null=True, verbose_name='первая сторона паспорта')),
                ('second_side_passport', models.URLField(blank=True, null=True, verbose_name='вторая сторона паспорта')),
                ('image', models.URLField(blank=True, null=True, verbose_name='Фото профиля')),
                ('driver_status', models.CharField(blank=True, choices=[('ready_to_work', 'ready_to_work'), ('has_work', 'has_work'), ('processed', 'processed'), ('not-processed', 'not-processed')], default='ready_to_work', max_length=50, null=True)),
                ('last_active_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Last active time')),
                ('car_data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trajectories.drivercardata')),
                ('card_data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver', to='billing.drivercarddata', verbose_name='данные карты водителя')),
            ],
        ),
    ]