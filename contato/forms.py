from django import forms

# Class formulário para iniciado

class ContatoForm(forms.Form):
    nome_completo = forms.CharField(max_length=60, help_text='Digite seu nome completo')
    email = forms.CharField(help_text='Digite seu e-mail')
    telefone = forms.IntegerField(help_text='Digite o número de telefone')
    hora_contato = forms.CharField(help_text='Selecione a hora para contato')
    mensagem = forms.CharField(help_text='Digite sua mensagem')
    
class ContatoAtualizarForm(forms.Form):
    nome_completo = forms.CharField(max_length=60, help_text='Digite seu nome completo')
    email = forms.CharField(help_text='Digite seu e-mail')
    telefone = forms.IntegerField(help_text='Digite o número de telefone')
    hora_contato = forms.CharField(help_text='Selecione a hora para contato')
    mensagem = forms.CharField(help_text='Digite sua mensagem')