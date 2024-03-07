from django.shortcuts import render
from django.http import HttpResponse
from base.forms import CadastroForm
from base.models import Cadastro
# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')


def cadastro(request):
    sucesso = False
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()  # aqui, tudo do formulario é salvo no banco de dados
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro.html', contexto)
