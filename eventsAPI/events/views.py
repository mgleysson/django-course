import datetime

from django.utils import timezone
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
        events = Event.objects.all()
        response = {'events_count': len(events)}
        return Response(data=response, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def all_events(self, request):
        events = Event.objects.all()
        serializer = self.get_serializer(events, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def events_with_tags(self, request):
        tags = Tag.objects.all()
        events = Event.objects.filter(tags__in=tags).distinct()
        serializer = self.get_serializer(events, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def next_events(self, request):
        next_time = timezone.now() + datetime.timedelta(days=5)
        current_time = timezone.now()
        events = Event.objects.filter(date__lte=next_time, date__gte=current_time)
        serializer = self.get_serializer(events, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def events_by_year(self, request):
        year_var = self.request.query_params.get('year')
        events = Event.objects.filter(date__year=year_var)
        serializer = self.get_serializer(events, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
