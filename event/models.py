from django.db import models
from django.core.exceptions import ValidationError


class Event(models.Model):
    day = models.DateField(verbose_name='Event day', help_text='Day of the event')
    start_time = models.TimeField(verbose_name='Starting time', help_text='Starting time')
    end_time = models.TimeField(verbose_name='Ending time', help_text='Ending time')
    notes = models.TextField(max_length=256, null=True, blank=True)

    class Meta:
        verbose_name = 'Scheduling'
        verbose_name_plural = 'Scheduling'

    def is_overlapin(self, event):
        overlap = False
        if self.start_time >= event.start_time and self.start_time <= event.end_time:
            overlap = True
        elif self.end_time >= event.start_time and self.end_time <= event.end_time:
            overlap = True
        elif self.start_time <= event.start_time and self.end_time >= event.end_time:
            overlap = True

        return overlap

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError('Ending time must be grater than starting time')
        existing_event = Event.objects.filter(day=self.day).exclude(id=self.id)
        for event in existing_event:
            if self.is_overlapin(event):
                raise ValidationError('Your events is overlaping.')

    def __str__(self):
        return f'{self.day}{self.start_time}-{self.end_time}'
