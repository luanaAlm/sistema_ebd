from django.contrib.auth.models import User
from django.db import models
# from apps.localidades.models import Localidade
from apps.pessoas.models import Cpf, Pessoa, Telefone
# from apps.turmas.models import Turma


class Aluno(Pessoa, Cpf, Telefone):
    ID_Aluno = models.AutoField(primary_key=True, null=False)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
