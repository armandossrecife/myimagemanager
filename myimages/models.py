from django.db import models
from django.contrib.auth.models import User

# Faz o upload da imagem para uma pasta (id) do usuario 
def upload_to(instance, filename):
    return f'images/{instance.user.id}/{filename}'

# Modelo da entidade Imagem
class Imagem(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to=upload_to)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nome