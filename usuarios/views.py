from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import CreateView, ListView, View
from django.core.urlresolvers import reverse_lazy
from django.contrib import auth
from labs.models import Laboratorio
from usuarios.models import Inscricao
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from usuarios.forms import RegistrarUsuarioForm
from django.contrib.auth.models import User

@login_required
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

class RegistrarUsuario(View):
    template_name = 'registrar.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            dados = form.data

            usuario = User.objects.create_user(dados['nome'], dados['email'], dados['senha'])

            perfil = Inscricao(nome=dados['nome'],
                               matricula=dados['matricula'],
                               curso=dados['curso'],
                               usuario=usuario)
            perfil.save()

        return render(request, 'index.html')

def get_perfil_logado(request):
    return request.user.perfil

@login_required
def reserva_laboratorio(request, laboratorio_id):
    dataEntrada = request.POST.get('dataEntrada')
    horaEntrada = request.POST.get('horaEntrada')
    horaSaida = request.POST.get('horaSaida')
    laboratorio = Laboratorio.objects.get(id=laboratorio_id)
    usuario_logado = get_perfil_logado(request)
    usuario_logado.reserva_laboratorio(laboratorio, dataEntrada, horaEntrada, horaSaida)
    return render(request, 'confirma_reserva.html')



