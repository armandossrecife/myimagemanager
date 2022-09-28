from django.db import models
from django.contrib.auth.models import User

def upload_to(instance, filename):
    return f'images/{instance.user.id}/{filename}'

class Imagem(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to=upload_to)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome