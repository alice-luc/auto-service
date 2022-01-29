from django.urls import path
from .views import *

urlpatterns = [
    path('service_detail/<slug:service_slug>', ServiceDetailView.as_view(), name='service_detail'),
    path('services/<slug:service_type_slug>', Services.as_view(), name='services'),
    # path('repair/', Repair.as_view(), name='repair'),
    # path('recovery/', Recovery.as_view(), name='recovery')
]
