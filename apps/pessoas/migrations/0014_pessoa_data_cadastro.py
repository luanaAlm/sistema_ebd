# Generated by Django 3.2.7 on 2021-10-05 18:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0013_auto_20211005_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
