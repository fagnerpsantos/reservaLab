from django.shortcuts import render
from laboratorios.models import Laboratorio

def index(request):
	return render(request, 'index.html')

def laboratorio(request, laboratorio_id):
	laboratorio = Laboratorio.objects.get(id=laboratorio_id)

	return render(request, 'laboratorio.html', { "laboratorio" : laboratorio})
