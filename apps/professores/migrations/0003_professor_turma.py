# Generated by Django 3.2.7 on 2021-09-30 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0002_remove_turma_date'),
        ('professores', '0002_rename_id_aluno_professor_id_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='turma',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='turmas.turma'),
            preserve_default=False,
        ),
    ]
