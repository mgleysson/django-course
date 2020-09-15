from rest_framework import serializers
from .models import Event, Comment, Tag


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'author', 'email', 'text', 'date', 'event')
        ordering = ('-date',)


class EventSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'date', 'event', 'text_priority', 'comments', 'tags')


class NewEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'date', 'event', 'priority', 'tags')


class TagSerializer(serializers.ModelSerializer):

    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ('id', 'title', 'information', 'events')



