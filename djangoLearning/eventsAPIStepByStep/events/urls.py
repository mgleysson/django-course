from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('events', viewset=views.EventViewSet)
router.register('comments', viewset=views.CommentViewSet)
router.register('tags', viewset=views.TagViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]