from django.db import models

class Critico(models.Model):
    nome = models.CharField(max_length=30)
    foto = models.ImageField(blank=True)
    email = models.EmailField(blank=False, max_length=30, )
    descricao = models.CharField(max_length=100)
    review = models.CharField(max_length=250)
    video = models.FileField(blank=True)

    def __str__(self):
        return self.nome