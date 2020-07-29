from practice.api.serializer import PracticeSerializer
from practice.models import Practice
# from rest_framework.generics import get_object_or_404
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class PracticesList(ListCreateAPIView):

    serializer_class = PracticeSerializer

    # TODO: rewrite filter
    def get_queryset(self):
        practices = Practice.objects.all()
        if 'from' in self.request.query_params:
            practices.filter(start_date=self.request.query_params['from'])
        if 'to' in self.request.query_params:
            practices.filter(start_date=self.request.query_params['to'])
        return practices


class PracticeView(RetrieveUpdateDestroyAPIView):

    def get(self, request, pk):
        pass

    def update(self, request, pk):
        pass

    def delete(self, request, pk):
        pass