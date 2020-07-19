from django.db import models
from django.core.exceptions import ValidationError


class Event(models.Model):
    day = models.DateField(verbose_name='Event day', help_text='Day of the event')
    start_time = models.TimeField(verbose_name='Starting time', help_text='Starting time')
    end_time = models.TimeField(verbose_name='Ending time', help_text='Ending time')
    notes = models.TextField(max_length=256, null=True)

    class Meta:
        verbose_name = 'Scheduling'
        verbose_name_plural = 'Scheduling'

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError('Ending time must be grater than starting time')
