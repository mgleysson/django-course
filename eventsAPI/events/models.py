from django.db import models

# Create your models here.


class Event(models.Model):

    priority_list = [
        ('0', 'Sem prioridade'),
        ('1', 'Normal'),
        ('2', 'Urgente'),
        ('3', 'Muito urgente')
    ]

    event = models.CharField(max_length=80)
    date = models.DateField()
    priority = models.CharField(max_length=1, choices=priority_list)

    def __str__(self):
        return self.event + ' - ' + str(self.date)
