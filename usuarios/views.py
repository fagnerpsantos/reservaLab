from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib import auth
from labs.models import Laboratorio
from usuarios.models import Inscricao
from models import Reserva
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.sessions.backends.db import SessionStore

def home(request):
        return render(request, 'index.html')

class Criar(CreateView):
        template_name = 'registrar.html'
        model = Inscricao
        success_url = reverse_lazy('index')

def get_perfil_logado(request):
    return Inscricao.objects.get(id=1)

def reserva_laboratorio(request, laboratorio_id):
    dataEntrada = request.POST.get('dataEntrada')
    horaEntrada = request.POST.get('horaEntrada')
    horaSaida = request.POST.get('horaSaida')
    laboratorio = Laboratorio.objects.get(id=laboratorio_id)
    usuario_logado = get_perfil_logado(request)
    usuario_logado.reserva_laboratorio(laboratorio, dataEntrada, horaEntrada, horaSaida)
    return render(request, 'confirma_reserva.html')

def login_usuario(request):
    login = request.POST.get('matricula')
    senha = request.POST.get('senha')

    usuario = Inscricao.objects.get(matricula=login)
    if(usuario):
        if(usuario.senha  == senha):
            return HttpResponseRedirect('/profile')
        else:
            return render(request, 'invalid.html')

def login_pagina(request):
    return render(request, 'login_usuario.html')

def historico(request):
    hist = Reserva()
    return render_to_response("profile.html", {'hist': Reserva.objects.all()})   