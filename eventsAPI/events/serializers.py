from rest_framework import serializers

from events.models import Event, Comment, Tag


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class NewCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id',)


class EventSerializer(serializers.ModelSerializer):

    comments = NewCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'event', 'date', 'text_priority', 'comments', 'tags')


class NewEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'event', 'date', 'priority', 'tags')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'



