from django.db import models
from practice.models import Practice


class Event(models.Model):
    day = models.DateField(verbose_name='Event day', help_text='Day of the event')
    start_time = models.TimeField(verbose_name='Starting time', help_text='Starting time')
    notes = models.TextField(max_length=256, null=True, blank=True)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Scheduling'
        verbose_name_plural = 'Scheduling'

    def __str__(self):
        return f'{self.day}{self.start_time}'
