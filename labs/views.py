from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Laboratorio
from forms import FormCadastroLaboratorio
from usuarios.models import Inscricao



def cadastraLab(request):
    if request.method == "POST":
        form = FormCadastroLaboratorio(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('confirma.html', {})
    else:
        form = FormCadastroLaboratorio()

    return render(request, "cadastra.html", {'form': form}, context_instance=RequestContext(request))

def lista_laboratorio(request):
    return render(request, 'lista_laboratorio.html', {'laboratorios' : Laboratorio.objects.all()})

def reservar(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(id=laboratorio_id)
    return render(request, 'reserva.html', { "laboratorio" : laboratorio})



