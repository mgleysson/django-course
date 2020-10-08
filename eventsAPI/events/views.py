from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from events.models import Event, Comment, Tag
from events.serializers import EventSerializer, CommentSerializer, NewEventSerializer, TagSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    # serializer_class = EventSerializer

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT'):
            return NewEventSerializer
        return EventSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
