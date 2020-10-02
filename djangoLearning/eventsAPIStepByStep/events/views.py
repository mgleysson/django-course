from django.shortcuts import render
from rest_framework import viewsets, filters

from .models import Event, Comment
from .serializers import CommentSerializer, EventSerializerWithComments, EventSerializerWithoutComments, \
    NewEventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT'):
            return NewEventSerializer
        return EventSerializerWithoutComments


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("event__id",)
