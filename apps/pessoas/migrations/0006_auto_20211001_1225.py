# Generated by Django 3.2.7 on 2021-10-01 15:25

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0005_auto_20211001_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cpf',
            fields=[
                ('ID_Cpf', models.AutoField(primary_key=True, serialize=False)),
                ('numero_cpf', cpf_field.models.CPFField(
                    max_length=14, unique=True, verbose_name='CPF')),
            ],
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='numero_cpf',
        ),
    ]