# Generated by Django 3.2.7 on 2021-10-01 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_alter_pessoa_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='numero_cpf',
            field=models.CharField(default=1, max_length=14, unique=True),
            preserve_default=False,
        ),
    ]
