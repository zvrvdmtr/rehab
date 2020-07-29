from django.contrib import admin
from event.models import Event


class EventAdmin(admin.ModelAdmin):

    fields = ['day', 'start_time', 'notes']
    list_display = ['day', 'start_time']


admin.site.register(Event, EventAdmin)
