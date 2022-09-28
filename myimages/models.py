from django.db import models
from django.contrib.auth.models import User

class Imagem(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome