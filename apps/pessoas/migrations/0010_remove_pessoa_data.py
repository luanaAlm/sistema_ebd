# Generated by Django 3.2.7 on 2021-10-02 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0009_alter_pessoa_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='data',
        ),
    ]
