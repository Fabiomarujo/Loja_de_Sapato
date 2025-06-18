from django.db import models
from django.utils import timezone

# Create your models here.
class Fornecedores(models.Model):
    codigo = models.CharField(help_text='Digite o código')
    nome = models.CharField(max_length=60, help_text='Digite o nome do produto')


def __str__(self):
    return f'{self.codigo} - {self.nome}'