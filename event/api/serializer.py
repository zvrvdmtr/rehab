from rest_framework import serializers
from event.models import Event
from practice.api.serializer import PracticeSerializer


class EventSerializer(serializers.ModelSerializer):

    practice = PracticeSerializer()

    class Meta:
        model = Event
        fields = '__all__'
