from django.contrib import admin
from event.models import Event


class EventAdmin(admin.ModelAdmin):

    fields = ['date', 'start_time', 'notes']
    list_display = ['date', 'start_time']


admin.site.register(Event, EventAdmin)
