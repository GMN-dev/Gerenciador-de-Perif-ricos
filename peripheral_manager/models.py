from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CadastroProduto(models.Model):
    TYPE_PERIPHERAL = (("entrada","Entrada"),( "saida","Saida"))
    nameProduct = models.CharField(max_length=250, verbose_name="Nome do Produto")
    description = models.TextField(verbose_name="Descrição", null=True, blank=True)
    typeProduct = models.CharField(max_length=250, choices=TYPE_PERIPHERAL, default="Entrada")
    registrationDate = models.DateTimeField(verbose_name="")


    def __str__(self):
        return self.nameProduct

class CadastroEquipamento(models.Model):
    category = models.ForeignKey(CadastroProduto, on_delete=models.PROTECT, verbose_name="Categoria")
    ticket = models.CharField(max_length=250, verbose_name="N° do Chamado:")
    heritage = models.CharField(max_length=12, verbose_name="Patrimônio:")
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Cadastrado por:")

    def __str__(self):
        return self.heritage

    class Meta:
        verbose_name = "Estoque"