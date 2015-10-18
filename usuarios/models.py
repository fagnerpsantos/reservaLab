from django.db import models

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
