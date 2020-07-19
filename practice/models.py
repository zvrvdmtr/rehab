from django.db import models
from event.models import Event


class Practice(models.Model):

    title = models.CharField(max_length=128, verbose_name='Prcatice title')
    descrioption = models.TextField(max_length=256,
                                    verbose_name='Practice description')
    reps = models.PositiveIntegerField(verbose_name='Reps number')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Practice'
        verbose_name_plural = 'Practices'
