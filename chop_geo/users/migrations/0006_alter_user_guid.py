# Generated by Django 5.0.8 on 2024-10-03 19:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_guid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='guid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
