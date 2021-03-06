from django.db import models
from django.utils import timezone


class Tag(models.Model):
    title = models.CharField(max_length=50)
    information = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-title',)


class Event(models.Model):

    priorities_list = (
        ('0', 'Sem prioridade'),
        ('1', 'Normal'),
        ('2', 'Urgente'),
        ('3', 'Muito Urgente')
    )

    event = models.CharField(max_length=80)
    date = models.DateTimeField()
    priority = models.CharField(max_length=1, choices=priorities_list)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)

    def __str__(self):
        return self.event

    @property
    def text_priority(self):
        for k, v in self.priorities_list:
            if k == self.priority:
                return v
        return ""


class Comment(models.Model):
    author = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.CharField(max_length=160)
    date = models.DateTimeField(default=timezone.now)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.author + ' - ' + str(self.date)

    class Meta:
        ordering = ('-date',)
