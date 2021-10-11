from django.db import models
from apps.pessoas.models import Pessoa
from apps.localidades.models import Localidade
from apps.turmas.models import Turma
from django.contrib.auth.models import User


class Secretario(Pessoa):
    ID_Secretario = models.AutoField(primary_key=True, null=False)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
