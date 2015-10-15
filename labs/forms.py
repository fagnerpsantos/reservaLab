from django import forms
from models import Laboratorio

class FormCadastroLaboratorio(forms.ModelForm):
    class Meta:
        model = Laboratorio