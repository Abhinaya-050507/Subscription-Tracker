from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_list, name='subscription_list'),
    path('add/', views.add_subscription, name='add_subscription'),
]
