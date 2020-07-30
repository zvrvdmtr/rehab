from django.core.management.base import BaseCommand
from event.models import Event
from practice.models import Practice


class Command(BaseCommand):

    help = 'Populate models with data'

    def handle(self, *args, **options):
        first_practice = Practice.objects.create(
            title='first',
            injury_type='Shoulder dislocation',
            reps=10,
            loops=10,
            description='Test description',
            start_time='20:00',
            start_date='2020-01-01',
            end_date='2020-02-01',
        )
        second_practice = Practice.objects.create(
            title='second',
            injury_type='Lag broke',
            reps=5,
            loops=5,
            description='Test description',
            start_time='20:00',
            start_date='2020-02-02',
            end_date='2020-03-01',
        )

        first_practice.save()
        second_practice.save()

        Event.objects.create(
            date='2020-01-01',
            start_time='20:00',
            notes='Test notes',
            practice_id=first_practice.id
        ).save()

        Event.objects.create(
            date='2020-02-02',
            start_time='20:00',
            notes='Test notes',
            practice_id=second_practice.id
        ).save()
