# Generated by Django 3.2.7 on 2021-10-02 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0006_auto_20211001_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('ID_Telefone', models.AutoField(primary_key=True, serialize=False)),
                ('telefone', models.CharField(max_length=13)),
            ],
        ),
    ]
