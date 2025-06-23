from django import forms

# Class formulário para iniciado

class FornecedorForm(forms.Form):    
    nome = forms.CharField(max_length=60, help_text='Digite o nome do fornecedor')
    
class FornecedorAtualizarForm(forms.Form):
    codigo = forms.CharField(required=True, help_text='Digite o código')
    nome = forms.CharField(max_length=60, help_text='Digite o nome do fornecedor')