from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from labs.models import Laboratorio

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
