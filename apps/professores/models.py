from django.db import models
from apps.localidades.models import Localidade
from apps.pessoas.models import Pessoa
from apps.turmas.models import Turma


class Professor(Pessoa, Localidade):
    ID_Professor = models.AutoField(primary_key=True, null=False)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Professores'

    def __str__(self):
        return self.nome
