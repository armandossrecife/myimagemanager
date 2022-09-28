from rest_framework import viewsets, generics
from myimages.models import Imagem
from myimages.serializer import ImagensSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser

class ImagemViewSet(viewsets.ModelViewSet):
    """Exibindo todas as imagens"""
    queryset = Imagem.objects.all()
    serializer_class = ImagensSerializer

class ImageListUserViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Imagem.objects.filter(user_id=self.kwargs['user_id'])
        return queryset
    serializer_class = ImagensSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user) 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer