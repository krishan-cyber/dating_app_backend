# Generated by Django 5.1.4 on 2025-02-15 03:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_alter_otp_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 15, 4, 0, 49, 869469, tzinfo=datetime.timezone.utc)),
        ),
    ]
