from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def mensagem(request):
    hora_atual = datetime.now().hour
    if 5 <= hora_atual < 12:
        mensagem = "Bom dia!"
    elif 12 <= hora_atual < 18:
        mensagem = "Boa tarde!"
    else:
        mensagem = "Boa noite!"
    return render(request, 'home.html', {'mensagem': mensagem})

def home(request):
    nome = "Antonio Hannesch"
    return render(request, 'home.html', {'nome':nome})

def saudacao(request, nome):
    mensagem = f'Olá, {nome}! Bem vindo(a) ao nosso  site.'
    return HttpResponse(mensagem)

def produtos(request, id_produto):
    produtos = {
        1:'Notebook',
        2:'Teclado',
        3:'Mouse',
    }
    produto = produtos.get(id_produto, "Produto não encontrado")
    return HttpResponse(f'Detalhes do produto: {produto}')

def produtos(request):
    produtos = ['Notebook', 'Teclado', 'Mouse', 'Fone', 'Celular']
    return render(request, 'produtos.html', {'produtos': produtos})