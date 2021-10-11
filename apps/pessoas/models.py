from django.db import models
from cpf_field.models import CPFField


class Cpf(models.Model):
    ID_Cpf = models.AutoField(primary_key=True, null=False)
    numero_cpf = CPFField('CPF', max_length=14, null=False,
                          unique=True)

    def __str__(self):
        return self.numero_cpf


class Pessoa(models.Model):
    ID_Pessoa = models.AutoField(primary_key=True, null=False)
    nome = models.CharField(max_length=30, null=False)
    sobrenome = models.CharField(
        max_length=100, null=False)
    data = models.DateField(max_length=8, verbose_name="Data de Nascimento")
    data_cadastro = models.DateTimeField(auto_now_add=True)

    # def maior(self):

    #     days_in_year = 365.2425
    #     age = int((self.data.today() - 18).days / days_in_year)

    #     if age >= 18:
    #         return self.data
    #     else:
    #         print('menor')

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    ID_Telefone = models.AutoField(primary_key=True, null=False)
    telefone = models.CharField(blank=False, null=False, max_length=13)


class Endereco(models.Model):
    STATE_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', ' Maranhão '),
        (' MT ', ' Mato Grosso '),
        (' MS ', ' Mato Grosso do Sul '),
        (' MG ', ' Minas Gerais '),
        (' PA ', ' Pará '),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima '),
        (' SC ', ' Santa Catarina '),
        (' SP ', ' São Paulo '),
        (' SE ', ' Sergipe '),
        (' TO ', ' Tocantins ')
    )

    endereco = models.CharField(max_length=100, blank=False, null=False)
    numero = models.IntegerField(null=True, blank=True, verbose_name="Número")
    complemento = models.CharField(
        max_length=1000, null=True, blank=True, verbose_name="Ponto de Referência")
    cep = models.CharField(max_length=9, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=False)
    municipio = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="Município")
    estado = models.CharField(max_length=100, choices=STATE_CHOICES)
