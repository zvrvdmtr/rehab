from django.contrib import admin
from practice.models import Practice


class PracticeAdmin(admin.ModelAdmin):

    fields = ['title', 'reps', 'event', 'descrioption']
    list_display = ['title', 'reps', 'event']


admin.site.register(Practice, PracticeAdmin)
