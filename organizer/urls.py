from django.urls import path
from . import views

app_name = 'organizer'

urlpatterns = [
    path('', views.index, name='index'),
]
