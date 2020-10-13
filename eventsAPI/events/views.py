from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from events.models import Event, Comment, Tag
from events.serializers import EventSerializer, CommentSerializer, NewEventSerializer, TagSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['event', 'tags__title', 'priority']
    ordering_fields = ['event']
    # serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT'):
            return NewEventSerializer
        return EventSerializer

    @action(methods=['GET'], detail=False)
    def stats2(self, request):
        permission_classes = (IsAdminUser,)
        events = Event.objects.all()
        response = {'events_count': len(events)}
        return Response(data=response, status=status.HTTP_200_OK)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
