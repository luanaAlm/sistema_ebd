# Generated by Django 3.2.7 on 2021-10-02 20:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0007_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 10, 2, 20, 45, 47, 821770, tzinfo=utc), max_length=8),
            preserve_default=False,
        ),
    ]
