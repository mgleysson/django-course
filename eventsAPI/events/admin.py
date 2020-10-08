from django.contrib import admin

# Register your models here.
from . import models
from .models import Event


# admin.site.register(models.Event)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event', 'date', 'priority',)
    list_display_links = ('event',)
    list_filter = ('date', 'priority',)
    list_editable = ('priority',)
    search_fields = ('event', 'date',)
