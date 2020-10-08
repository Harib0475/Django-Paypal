from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('paypal/pay/<pk>/', pay, name="pay"),
    path('paypal/create/<id>/', create, name="paypal-create"),
    path('paypal/<order_id>/capture/<id>/', capture, name="paypal-capture"),
    path('paypal/client-id/', getClientId, name="client-id")
]
