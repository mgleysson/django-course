from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from events import views

router = routers.DefaultRouter()
router.register('events', viewset=views.EventViewSet)
router.register('comments', viewset=views.CommentViewSet)
router.register('tags', viewset=views.TagViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth-token', obtain_auth_token)
]