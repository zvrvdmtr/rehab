from rest_framework import serializers
from event.models import Event


class EventSerializer(serializers.Serializer):

    day = serializers.DateField()
    start_time = serializers.TimeField()
    notes = serializers.CharField()

    def create(self, validate_data):
        return Event.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.day = validate_data.get('day')
        instance.start_time = validate_data.get('start_time')
        instance.notes = validate_data.get('notes')
        instance.save()
        return instance
