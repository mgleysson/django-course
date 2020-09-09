from rest_framework import serializers
from .models import Event, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'author', 'email', 'text', 'date', 'event')
        ordering = ('-date',)


class EventSerializer(serializers.ModelSerializer):

    comment_event = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'date', 'event', 'text_priority', 'comment_event')


class NewEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'date', 'event', 'priority')



