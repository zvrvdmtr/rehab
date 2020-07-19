from django.urls import path
from event.api.views import EventsList, EventView

urlpatterns = [
    path('events/', EventsList.as_view()),
    path('event/<int:pk>', EventView.as_view()),
]
