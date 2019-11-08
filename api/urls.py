from django.urls import path

from .views import *

app_name = 'api'

urlpatterns = [
    path('/sith', GetSithInfo.as_view(), name='main'),
    path('/planet', GetPlanet.as_view(), name='get_planet'),
    path('/recruiter', AddRecruiter.as_view(), name='add_recruiter'),
    path('/questions', GetQuestions.as_view(), name='get_questions'),
    path('/answer', AddAnswer.as_view(), name='add_answer'),
    path('/single_sith/', SingleSith.as_view(), name='single_sith'),
    path('/enroll', EnrollRecruit.as_view(), name='enroll'),

]