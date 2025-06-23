from django.db import models

# Create your models here.
class Clientes(models.Model):
    id = models.AutoField(primary_key=True, help_text='Identificação do Cliente')
    cpf = models.CharField(max_length=11, help_text='Digite o CPF')
    nome = models.CharField(max_length=70, help_text='Digite o Nome do Aluno')
    endereco = models.CharField(max_length=100, help_text='Digite o endereço')
    telefone = models.CharField(max_length=11, help_text='Digite o número de telefone')
    uf = models.CharField(max_length=2, help_text='Escolha seu estado')
    cidade = models.CharField(max_length=50, help_text='Digite sua cidade')
    genero = models.CharField(max_length=1, help_text='Escolha seu gênero')
    contato = models.CharField(max_length=100, help_text='Escolha forma de contato')
    email_cliente = models.CharField(max_length=100, help_text='Digite seu e-mail')
    senha = models.CharField(max_length=256, help_text='Informe a senha:')


def __str__(self):
    return f'{self.id} - {self.cpf} - {self.nome} - {self.endereco} - {self.telefone} - {self.uf} - {self.cidade} - {self.genero} - {self.contato} - {self.email_cliente} - {self.senha}'