from rest_framework import serializers
from practice.models import Practice


class PracticeSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=128)
    injury_type = serializers.CharField(max_length=128)
    reps = serializers.IntegerField()
    loops = serializers.IntegerField()
    descrioption = serializers.CharField(max_length=256)
    start_time = serializers.TimeField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def create(self, validate_data):
        return Practice.objects.create(**validate_data)
