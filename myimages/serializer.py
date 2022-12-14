from pyexpat import model
from rest_framework import serializers
from dataclasses import field, fields
from myimages.models import Imagem
from django.contrib.auth.models import User

# Serializa os dados da imagem
class ImagensSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    creator_id = serializers.ReadOnlyField(source='creator.id')
    class Meta:
        model = Imagem
        fields = ['id', 'nome', 'foto', 'user', 'creator', 'creator_id']

# Serializa os dados do usuario
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']