from django.urls import path

from . import views

app_name = 'sith'
urlpatterns = [
    path('main', views.main, name='main'),

]