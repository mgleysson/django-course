from rest_framework import serializers
from .models import Event, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'email', 'text', 'date', 'event')


class EventSerializerWithComments(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'event', 'date', 'text_priority', 'comments')


class EventSerializerWithoutComments(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'event', 'date', 'text_priority')



