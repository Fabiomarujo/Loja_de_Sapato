from django import forms

# Class formulário para iniciado

class ProdutoForm(forms.Form):    
    codigo = forms.IntegerField(required=True, help_text='Digite o código')
    nome = forms.CharField(max_length=60, help_text='Digite o Nome do Aluno')
    preco_compra = forms.FloatField(help_text='Digite o preço de compra')
    preco_venda = forms.FloatField(help_text='Digite o preço de venda')
    cor = forms.ImageField(help_text='Selecione a cor')
    tamanho = forms.CharField(help_text='Escolha o tamanho')
    imagem = forms.CharField(help_text='Nome da imagem do produto')
    
class ProdutoAtualizarForm(forms.Form):
    codigo = forms.IntegerField(required=True, help_text='Digite o código')
    nome = forms.CharField(max_length=60, help_text='Digite o nome do Aluno')
    preco_compra = forms.FloatField(help_text='Digite o preço de compra')
    preco_venda = forms.FloatField(help_text='Digite o preço de venda')
    cor = forms.ImageField(help_text='Selecione a cor')
    tamanho = forms.CharField(help_text='Escolha o tamanho')
    imagem = forms.CharField(help_text='Nome da imagem do produto')