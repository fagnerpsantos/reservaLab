from django.db import models

class Inscricao(models.Model):
        nome = models.CharField(max_length=100)
        matricula = models.CharField('matricula', max_length=11, unique=True)
        senha = models.CharField(max_length=20)
        curso = models.CharField(max_length=30)
        criado_em = models.DateTimeField('criado em', auto_now_add=True)


        class Meta:
                ordering = ['criado_em']
                verbose_name = (u'nome')
                verbose_name_plural = (u'nomes')

        def __unicode__(self):
                return self.nome