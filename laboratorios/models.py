from django.db import models

class Laboratorio(models.Model):
	bloco = models.CharField(max_length=1, null=False)
	sala = models.CharField(max_length=2, null=False)