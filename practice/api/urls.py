from django.urls import path
from practice.api.views import PracticesList, PracticeView

urlpatterns = [
    path('practices_list/', PracticesList.as_view()),
    path('practice/<int:pk>', PracticeView.as_view()),
]
