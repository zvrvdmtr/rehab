from event.api.serializer import EventSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from event.models import Event


class EventsList(APIView):

    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            event_saved = serializer.save()
            return Response({'New event created': event_saved.day}, status=status.HTTP_201_CREATED)


class EventView(APIView):

    def get(self, request, pk):
        event = get_object_or_404(Event.objects.all(), id=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        event = get_object_or_404(Event.objects.all(), id=pk)
        data = request.data
        serializer = EventSerializer(instance=event, data=data)
        if serializer.is_valid(raise_exception=True):
            saved_event = serializer.save()
            return Response({'Event updated': saved_event.day}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        event = get_object_or_404(Event.objects.all(), id=pk)
        event.delete()
        return Response({'Event deleted'}, status=status.HTTP_204_NO_CONTENT)
