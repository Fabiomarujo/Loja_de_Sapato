from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    codigo = models.CharField(help_text='Digite o código')
    nome = models.CharField(max_length=60, help_text='Digite o nome do fornecedor')


def __str__(self):
    return f'{self.codigo} - {self.nome}'