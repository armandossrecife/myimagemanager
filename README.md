# Projeto API MyImages

API que publica os seguintes serviços

### Lista todos os usuarios
GET
/users/
Read Users

### Cadastra um novo usuario
POST
/users/
Create User

### Faz a autenticação de um usuário já registrado
POST
/users/authentication
My Authentication

### Mostra os dados de um usuário
GET
/users/{user_id}
Read User

### Lista todas as imagens
GET
/images/
Read Images

### Lista as imagens de um usuário
GET
/users/{user_id}/images/
Read Images From User

### Mostra os dados da imagem de um usuário
GET
/users/{user_id}/images/{image_id}
Read Image From User

### Remove a imagem de um usuário
DELETE
/users/{user_id}/images/{image_id}
Delete Image From User

### Retorna o arquivo da imagem de um usuário
GET
/users/{user_id}/images/{image_id}/file
Get Image From User

### Faz o upload da imagem de um usuário
POST
/users/{user_id}/images/{name_file}
Create Upload File

### Faz o upload da lista de imagens de um usuário
POST
/users/{user_id}/images/uploadfiles/
Create Upload Files (edited) 

## 1. Cria um novo projeto 

django-admin startproject myimagemanager

obs: 
- sincronizar versão do Django
- sincronizar versão do DjangoRest

## 2. Executar o servidor 

python manage.py runserver

## 3. Cria o app myimages

python3 manage.py startapp myimages

obs: padronizar estrutura do projeto e apps
- verificar a estrutura (diretorios e configuração) do projeto principal
- verificar a estrutura (diretorios e configuração) do app 

## 4. Cria o superusuario do site admin

python3 manage.py createsuperuser

## 5. Faz a migração dos modelos para o banco

python3 manage.py makemigrations

## 6. Sobe as modificações dos modelos no banco configurado

python3 manage.py migrate

## 7. Cria o usuario admin

python3 manage.py createsuperuser

--- Referente ao DjangoRest --- 

## 8. No arquivo settings.py.

### 8.1 Registra a aplicação rest_framework.
### 8.2 Registra a aplicação myimages.
### 8.3 Configura a linguagem e time_zone.
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

### 8.4 Cria as constantes para armazenar arquivos de media.

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

MEDIA_URL = '/media/'

## 9. No arquivo models.py

- Cria o modelo Imagem 

### 9.1. Faz a migração dos modelos para o banco

python3 manage.py makemigrations

### 9.2. Sobe as modificações dos modelos no banco configurado

python3 manage.py migrate

## 10. Em serializers.py cria as classes que serao serializadas juntamente com seus atributos.
- Cria o ImagensSerializer
- Cria o UserSerializer

## 11. Cria os viewsets que serao publicados na api juntamente com suas informações.
- Cria o ImagemViewSet
- Cria o ImageListUserViewSet
- Cria o UserViewSet

## 12. Dentro a app myimages cria o arquivo urls.py para registrar as rotas da aplicação myimages.

## 13. Configura o arquivo urls.py do projeto para para incluir as urls da aplicação myimages.

## 14. Adiciona MEDIA_URL e MEDIA_ROOT no urlpatterns do arquivo urls.py do projeto para poder guardar as imagens.

## 15. Executar o servidor da api

python manage.py runserver

Acesse http://localhost:8000/myimages

## 16. Caso queira limpar o banco (apaga todos os dados das tabelas)

python3 manage.py flush

Obs: é preciso recriar o usuario admin

## Referencias:

Django - [Site](https://www.djangoproject.com/)

Django Rest - [Site](https://www.django-rest-framework.org/)

Upload de imagens em uma API Rest - [Alura](https://www.alura.com.br/artigos/django-upload-de-imagens-em-uma-api-rest)

Salvar imagem em uma pasta (id) do usuario [dev.to](https://dev.to/thomz/uploading-images-to-django-rest-framework-from-forms-in-react-3jhj)

Model field - [Django Doc](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.FileField)