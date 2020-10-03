from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register('events', viewset=views.EventViewSet)
router.register('comments', viewset=views.CommentViewSet)
router.register('tags', viewset=views.TagViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-token-auth', obtain_auth_token, name='api_token_auth')
]