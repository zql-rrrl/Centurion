from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test),
    path('get_habit/', views.get_habit),
]
