from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='workout'),
    path('routines/add', views.routine_create, name='routine_create_form'),
    path('routines/<int:pk>/edit', views.routine_edit, name='routine_edit_form'),
    path('routines/<int:pk>/delete', views.routine_delete, name='routine_delete'),
    path('routines/<int:pk>', views.routine_details, name='routine_details'),
    path('schedule/', views.CalendarView.as_view(), name='calendar'), 
]




