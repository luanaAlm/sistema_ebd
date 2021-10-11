from django.db import models
# from apps.secretarios.models import Secretario


class Turma(models.Model):
    MODALIDADE_CHOICES = (
        ('Adolescentes', 'Adolescentes'),
        ('Adulto', 'Adulto'),
        ('Infantil', 'Infantil'),
        ('Jovens', 'Jovens'),
        ('Juvenis', 'Juvenis'),
        ('Pré-Adolescentes', 'Pré-Adolescentes'),
    )
    ID_Turma = models.AutoField(primary_key=True, null=False)
    turma = models.CharField(max_length=45, null=False)
    modalidade = models.CharField(max_length=100, choices=MODALIDADE_CHOICES)
    # pert_secret = models.ForeignKey(
    #     Secretario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.turma
