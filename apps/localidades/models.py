from django.db import models


class Localidade(models.Model):

    ID_Localidade = models.AutoField(primary_key=True, null=False)
    nomeLocalidade = models.CharField(max_length=100, verbose_name="Igreja")

    def __str__(self):
        return self.nomeLocalidade
