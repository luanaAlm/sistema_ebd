# Generated by Django 3.2.7 on 2021-09-30 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoas.pessoa')),
                ('ID_Aluno', models.AutoField(primary_key=True, serialize=False)),
            ],
            bases=('pessoas.pessoa',),
        ),
    ]
