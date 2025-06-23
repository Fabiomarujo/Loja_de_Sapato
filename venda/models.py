from django.db import models
# import timezone

# Create your models here.
class Venda(models.Model):
    numero = models.IntegerField(help_text='Digite o numero')
    data_venda = models.DateTimeField(null=False, help_text='Informe a data da venda')
    valor_venda = models.FloatField(help_text='Digite o valor de venda')
    cliente_cpf = models.IntegerField(help_text='Informe o cpf do cliente')
    
# class Item_Venda(models.Model):
    venda_numero = models.IntegerField(help_text='Numero da venda')
    produto_codigo = models.IntegerField(help_text='Código do produto') 
    quantidade = models.IntegerField(help_text='Digite a quantidade')
    preco_venda = models.FloatField(help_text='Preço da venda')

def __str__(self):
    return f'{self.numero} - {self.data_venda} - {self.valor_venda} - {self.cliente_cpf} - {self.venda_numero} - {self.produto_codigo} - {self.quantidade} - {self.preco_venda}'