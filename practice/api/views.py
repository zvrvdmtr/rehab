from practice.api.serializer import PracticeSerializer
from practice.models import Practice
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class PracticesList(ListCreateAPIView):

    serializer_class = PracticeSerializer

    # TODO: rewrite filter
    def get_queryset(self):
        practices = Practice.objects.all()
        if 'from' in self.request.query_params:
            practices.filter(start_date__gte=self.request.query_params['from'])
        if 'to' in self.request.query_params:
            practices.filter(end_date__lte=self.request.query_params['to'])
        return practices


class PracticeView(RetrieveUpdateDestroyAPIView):

    serializer_class = PracticeSerializer
    queryset = Practice.objects.all()
