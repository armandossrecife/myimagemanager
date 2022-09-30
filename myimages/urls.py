from django.urls import path
from rest_framework import routers
from .views import ImagemViewSet, ImageListUserViewSet, UserViewSet, ImageListUserImageViewSet, ImageDetailUser, UploadImages

router = routers.DefaultRouter()
router.register('images', ImagemViewSet, basename='images')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('users/<int:user_id>/images/', ImageListUserViewSet.as_view()),
    path('users/<int:user_id>/images/<int:image_id>/', ImageListUserImageViewSet.as_view()),
    path('users/<int:user_id>/images/<int:image_id>/file/', ImageDetailUser),
    path('users/<int:user_id>/images/uploadfiles/', UploadImages.as_view()),    
]

urlpatterns += router.urls