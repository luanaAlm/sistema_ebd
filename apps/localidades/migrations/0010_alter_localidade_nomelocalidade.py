# Generated by Django 3.2.7 on 2021-10-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localidades', '0009_alter_localidade_nomelocalidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localidade',
            name='nomeLocalidade',
            field=models.CharField(max_length=100, verbose_name='Igreja'),
        ),
    ]