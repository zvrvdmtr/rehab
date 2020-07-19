from django.contrib import admin
from event.models import Event


class EventAdmin(admin.ModelAdmin):

    fields = ['day', 'start_time', 'end_time', 'notes']


admin.site.register(Event, EventAdmin)
