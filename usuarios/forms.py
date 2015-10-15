from django import forms
from models import Inscricao

class InscricaoForm(forms.ModelForm):

        class Meta:
                model = Inscricao