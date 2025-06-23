from django.db import models
import timezone

# Create your models here.
class Venda(models.Model):
    numero = models.IntegerField(max_length='256', help_text='Digite o numero')
    data_venda = models.DateTimeField(null=False, default=timezone.now(), help_text='Informe a data da venda')
    valor_venda = models.FloatField(help_text='Digite o valor de venda')
    cliente_cpf = models.CharField(max_length='11', help_text='Informe o cpf do cliente')
    
# class Item_Venda(models.Model):
    venda_numero = models.IntegerField(max_length='256', help_text='Numero da venda')
    produto_codigo = models.CharField(max_length='256', help_text='Código do produto') 
    quantidade = models.IntegerField(max_length='10', help_text='Digite a quantidade')
    preco_venda = models.FloatField(help_text='Preço da venda')

def __str__(self):
    return f'{self.numero} - {self.data_venda} - {self.valor_venda} - {self.cliente_cpf} - {self.venda_numero} - {self.produto_codigo} - {self.quantidade} - {self.preco_venda}'