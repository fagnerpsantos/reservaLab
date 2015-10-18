from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib import auth
from usuarios.models import Inscricao
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf


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
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)



def authView(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/lista_laboratorio')
    else:
        return render(request, 'invalid.html')
