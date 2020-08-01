from event.api.serializer import EventSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from event.models import Event
from rest_framework.permissions import IsAuthenticated


class EventsList(ListCreateAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        practices = Event.objects.all()
        if 'from' in self.request.query_params:
            practices.filter(event_date__gte=self.request.query_params['from'])
        if 'to' in self.request.query_params:
            practices.filter(event_date__lte=self.request.query_params['to'])
        return practices


class EventView(RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Event.objects.all()
    serialiser = EventSerializer
