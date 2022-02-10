from django.urls import path
from . import views

app_name = 'organizer'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task', views.add_task, name='add-task'),
    path('customer_list', views.customer_list, name='customer-list'),
    path('customer', views.customer, name='customer'),
]
