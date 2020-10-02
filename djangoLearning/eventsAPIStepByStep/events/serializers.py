from rest_framework import serializers
from .models import Event, Comment, Tag


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
        fields = ('id', 'event', 'date', 'text_priority', 'tags')


class NewEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'event', 'date', 'priority', 'tags')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'title', 'information')



