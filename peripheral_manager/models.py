from random import choices
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField

# Create your models here.
class CadastroProduto(models.Model):
    TYPE_PERIPHERAL = (("entrada","Entrada"),( "saida","Saida"))
    nomeProduto = models.CharField(max_length=250, verbose_name="Nome do Produto")
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    tipo = models.CharField(max_length=250, choices=TYPE_PERIPHERAL, default="Entrada")
    autor = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Cadastrado por Field:")

    def __str__(self):
        return self.nomeProduto

