# Generated by Django 5.0.8 on 2024-08-27 17:12

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleTrajectory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trajectories', to='trajectories.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleTrajectoryRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trajectory', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='trajectories.vehicle')),
            ],
        ),
    ]
