# Generated by Django 5.1.4 on 2025-02-20 04:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_alter_otp_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 20, 4, 25, 45, 742864, tzinfo=datetime.timezone.utc)),
        ),
    ]
