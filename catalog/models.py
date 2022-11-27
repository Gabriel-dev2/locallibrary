from django.db import models

# Create your models here.

class LivrosModel(models.Model):
    nome = models.CharField(max_length=200)
    autor  = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=9, decimal_places=2, default="0")