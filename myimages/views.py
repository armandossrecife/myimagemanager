from rest_framework import viewsets, generics
from myimages.models import Imagem
from myimages.serializer import ImagensSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse

# Lista todas as imagens cadastradas
class ImagemViewSet(viewsets.ModelViewSet):
    """Exibindo todas as imagens"""
    queryset = Imagem.objects.all()
    serializer_class = ImagensSerializer

# Lista todas as imagens de um usuario
class ImageListUserViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Imagem.objects.filter(user_id=self.kwargs['user_id'])
        return queryset
    serializer_class = ImagensSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user) 

# Mostra os dados de uma imagem
class ImageListUserImageViewSet(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Imagem.objects.filter(id=self.kwargs['image_id'])
        serializer = ImagensSerializer(queryset[0])
        return Response(serializer.data, status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        queryset = Imagem.objects.filter(id=self.kwargs['image_id']).first()
        queryset.delete()
        return Response(status.HTTP_200_OK)

# Retorna o arquivo da imagem
def ImageDetailUser(request, user_id, image_id):
    image = Imagem.objects.get(id=image_id)
    img = open(image.foto.path, 'rb')
    return FileResponse(img)

# Faz o upload da imagem
class UploadImages(generics.CreateAPIView):
    serializer_class = ImagensSerializer
    def post(self, request, *args, **kwargs):
        name_file = request.data['nome']
        user_id = request.data['user']
        image_user = request.data['foto']
        user = User.objects.filter(id=user_id)
        image = Imagem.objects.filter(user=user_id).filter(nome=name_file)
        if not user:
            return Response({'erro': 'Usuário informado não existe!'}, status=status.HTTP_400_BAD_REQUEST)
        if image:
            return Response({'erro': 'Esse nome já existe!'}, status=status.HTTP_400_BAD_REQUEST)
        if not image_user:
            return Response({'erro': 'Imagem não pode ser vazia!'}, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)

# para testar o upload do arquivo armando.jpg via curl
# curl -i -X POST -H "Content-Type: multipart/form-data" -F "foto=@/pastadaimagem/armando.jpg" -F "user=1" -F "nome=armando.jpg" http://localhost:8000/myimages/users/1/images/uploadfiles

# Lista os usuarios cadastrados
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer