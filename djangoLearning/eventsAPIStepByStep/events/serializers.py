from rest_framework import serializers
from .models import Event, Comment


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'event', 'date', 'text_priority')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'email', 'text', 'date', 'event')
