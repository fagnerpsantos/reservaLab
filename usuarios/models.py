from django.db import models
from labs.models import Laboratorio
from django.contrib.auth.models import User

class Inscricao(models.Model):
        nome = models.CharField(max_length=100)
        matricula = models.CharField('matricula', max_length=11, unique=True)
        curso = models.CharField(max_length=30)
        usuario = models.OneToOneField(User, related_name="perfil")


        def email(self):
            return self.usuario.email

        class Meta:
                ordering = ['nome']
                verbose_name = (u'Registro')
                verbose_name_plural = (u'Registros')

        def __unicode__(self):
                return self.nome

        def reserva_laboratorio(self, laboratorio, dataEntrada, horaEntrada, horaSaida):
            reserva = Reserva(solicitante=self, laboratorio=laboratorio, dataEntrada = dataEntrada, horaEntrada = horaEntrada, horaSaida = horaSaida)
            reserva.save()
            laboratorio.disponivel = False
            laboratorio.save()

class Reserva(models.Model):
        solicitante = models.ForeignKey(Inscricao)
        laboratorio = models.ForeignKey(Laboratorio)
        dataEntrada = models.CharField(max_length=10)
        horaEntrada = models.CharField(max_length=10)
        horaSaida = models.CharField(max_length=10)
