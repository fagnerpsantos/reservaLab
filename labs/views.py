from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Laboratorio
from forms import FormCadastroLaboratorio



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