from django.urls import path
from . import views

urlpatterns =[
    path('advisor/',views.showformdata),
]