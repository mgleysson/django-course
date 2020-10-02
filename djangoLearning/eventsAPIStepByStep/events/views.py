from django.shortcuts import render
from rest_framework import viewsets, filters

from .models import Event, Comment
from .serializers import CommentSerializer, EventSerializerWithComments, EventSerializerWithoutComments


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    #serializer_class = EventSerializerWithComments
    serializer_class = EventSerializerWithoutComments


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("event__id",)
