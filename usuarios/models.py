from django.db import models
from labs.models import Laboratorio

class Inscricao(models.Model):
        nome = models.CharField(max_length=100)
        matricula = models.CharField('matricula', max_length=11, unique=True)
        senha = models.CharField(max_length=20)
        curso = models.CharField(max_length=30)

        class Meta:
                ordering = ['nome']
                verbose_name = (u'Registro')
                verbose_name_plural = (u'Registros')

        def __unicode__(self):
                return self.nome

        def reserva_laboratorio(self, laboratorio, dataEntrada, horaEntrada, horaSaida):
            reserva = Reserva(solicitante=self, laboratorio=laboratorio, dataEntrada = dataEntrada, horaEntrada = horaEntrada, horaSaida = horaSaida, disponivel = False)
            reserva.save()

class Reserva(models.Model):
        solicitante = models.ForeignKey(Inscricao)
        laboratorio = models.ForeignKey(Laboratorio)
        dataEntrada = models.CharField(max_length=10)
        horaEntrada = models.CharField(max_length=10)
        horaSaida = models.CharField(max_length=10)
        disponivel = models.BooleanField(default=True)
