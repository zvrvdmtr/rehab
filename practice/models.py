from django.db import models
from django.core.exceptions import ValidationError


class Practice(models.Model):

    title = models.CharField(max_length=128, verbose_name='Prcatice title')
    injury_type = models.CharField(max_length=128, verbose_name='Injury type')
    reps = models.PositiveIntegerField(verbose_name='Reps number')
    loops = models.PositiveIntegerField(verbose_name='Loops number')
    descrioption = models.TextField(max_length=256,
                                    verbose_name='Practice description')
    start_time = models.TimeField(verbose_name='Время начала')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')

    class Meta:
        verbose_name = 'Practice'
        verbose_name_plural = 'Practices'

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start date must be less than end date')

    def __str__(self):
        return self.title
