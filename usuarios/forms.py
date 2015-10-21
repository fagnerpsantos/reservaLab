from django import forms
from django.contrib.auth.models import User

class RegistrarUsuarioForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.CharField(required=True)
    senha = forms.CharField(required=True)
    matricula = forms.CharField(required=True)
    curso = forms.CharField(required=True)


    def is_valid(self):
        valid = True
        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_erro('Dados incorretos')
            valid = False

        user_exists = User.objects.filter(username=self.data['nome']).exists()

        if user_exists:
            self.adiciona_erro('Usuario cadastrado')
            valid = False

        return valid

    def adiciona_erro(self, message):
        erros = self._e.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        erros.append(message)