from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .serializers import EventSerializer, CommentSerializer, NewEventSerializer
from .models import Event, Comment


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT'):
            return NewEventSerializer
        return EventSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('event__id',)
    permission_classes = (IsAuthenticated,)


