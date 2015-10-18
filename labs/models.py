from django.db import models

class Laboratorio(models.Model):
        bloco = models.CharField(max_length=1)
        sala = models.CharField(max_length=2)
        nome = models.CharField(max_length=30)
        disponivel = models.BooleanField(default=True)

        def __unicode__(self):
            return self.nome


