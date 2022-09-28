from django.urls import path
from rest_framework import routers
from .views import ImagemViewSet, ImageListUserViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('images', ImagemViewSet, basename='images')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('users/<int:user_id>/images/', ImageListUserViewSet.as_view()),
]

urlpatterns += router.urls