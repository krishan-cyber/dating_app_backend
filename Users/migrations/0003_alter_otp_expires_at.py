# Generated by Django 5.1.4 on 2025-02-14 03:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_otp_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 14, 4, 5, 59, 943714, tzinfo=datetime.timezone.utc)),
        ),
    ]
