# Generated by Django 3.2.7 on 2021-10-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0007_alter_aluno_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data',
            field=models.DateField(max_length=8, verbose_name='Data de Nascimento'),
        ),
    ]
