
from django.db import models
from django.utils import timezone

# Create your models here.
class Clientes(models.Model):
    cpf = models.CharField(help_text='Digite o CPF')
    nome = models.CharField(max_length=60, help_text='Digite o Nome do Aluno')
    endereco = models.CharField(help_text='Digite o endereço')
    telefone = models.IntegerField(help_text='Digite o número de telefone')
    estado = models.CharField(help_text='Escolha seu estado')
    cidade = models.CharField(help_text='Digite sua cidade')
    genero = models.CharField(help_text='Escolha seu gênero')
    contato = models.CharField(help_text='Escolha forma de contato')
    email_cliente = models.CharField(help_text='Digite seu e-mail')
    nome_usuario = models.CharField(help_text='')
    senha = models.CharField(help_text='')


def __str__(self):
    return f'{self.cpf} - {self.nome} - {self.endereco} - {self.telefone} - {self.estado} - {self.cidade} - {self.genero} - {self.contato} - {self.email_cliente} - {self.nome_usuario} - {self.senha}'