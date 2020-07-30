from rest_framework import serializers
from practice.models import Practice


class PracticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Practice
        fields = '__all__'
