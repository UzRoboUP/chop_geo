# Generated by Django 5.0.8 on 2024-10-14 06:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_user_guid_remove_user_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='guid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('processing', 'Processing'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('go_to_service', 'Go to service')], default='processing', max_length=50),
        ),
    ]
