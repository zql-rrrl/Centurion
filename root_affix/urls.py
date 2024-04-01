from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test),
    path('very_high_root/', views.very_high_root),
]
