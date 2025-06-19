from django.db import models
from django.utils import timezone

# Create your models here.
class Venda(models.Model):
    codigo = models.CharField(help_text='Digite o código')
    nome = models.CharField(max_length=60, help_text='Digite o Nome do Aluno')
    preco_compra = models.CharField(help_text='Digite o preço de compra')
    preco_venda = models.CharField(help_text='Digite o preço de venda')
    cor = models.IntegerField(help_text='Selecione a cor')
    data_fabricacao = models.DateField(help_text='Escolha a data de fabricação')
    imagem = models.CharField(help_text='Nome da imagem do produto')


def __str__(self):
    return f'{self.codigo} - {self.nome} - {self.preco_compra} - {self.preco_venda} - {self.cor} - {self.data_fabricacao} - {self.imagem}'