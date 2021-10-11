# Generated by Django 3.2.7 on 2021-10-01 15:10

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0004_remove_pessoa_cpf'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cpf',
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='numero_cpf',
            field=cpf_field.models.CPFField(max_length=14, unique=True),
        ),
    ]
