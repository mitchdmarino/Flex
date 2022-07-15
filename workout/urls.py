from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='workout_index')
]

