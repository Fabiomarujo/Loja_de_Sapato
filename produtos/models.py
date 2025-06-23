from django.db import models
from django.utils import timezone

# Create your models here.
class Produtos(models.Model):
    codigo = models.IntegerField(help_text='Digite o código')
    nome = models.CharField(max_length=60, help_text='Digite o Nome do Aluno')
    preco_compra = models.FloatField(help_text='Digite o preço de compra')
    preco_venda = models.FloatField(help_text='Digite o preço de venda')
    cor = models.ImageField(help_text='Selecione a cor')
    tamanho = models.CharField(help_text='Escolha o tamanho')
    imagem = models.CharField(help_text='Nome da imagem do produto')


def __str__(self):
    return f'{self.codigo} - {self.nome} - {self.preco_compra} - {self.preco_venda} - {self.cor} - {self.tamanho} - {self.imagem}'