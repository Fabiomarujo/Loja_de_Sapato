from django.shortcuts import render

# Create your views here.
def listar(request):
    return render(request, 'login/listarLogin.html')

def cadastrar(request):
    return render(request, 'login/cadastroLogin.html')
    
    