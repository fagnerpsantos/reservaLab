from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

from usuarios.models import Inscricao

def home(request):
        return render(request, 'index.html')

class Criar(CreateView):
        template_name = 'registrar.html'
        model = Inscricao
        success_url = reverse_lazy('listar')

class Lista(ListView):
        template_name = 'lista.html'
        model = Inscricao
        context_object = 'nome'

def login(request):
    return render(request, 'login.html')