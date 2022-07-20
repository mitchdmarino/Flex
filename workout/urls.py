from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='workout'),
    path('routines/add', views.routine_create, name='routine_create_form'),
    path('routines/<int:pk>/edit/', views.routine_edit, name='routine_edit_form'),
    path('routines/<int:pk>/delete/', views.routine_delete, name='routine_delete'),
    path('routines/<int:pk>/', views.routine_details, name='routine_details'),
    path('schedule/', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.workout, name='schedule_new_workout'), 
    path('event/<int:pk>/edit/', views.workout, name='edit_workout'),
    path('event/<int:pk>/', views.workout_details, name='workout_details'),
    path('event/<int:pk>/complete/', views.complete_workout, name="complete_workout"),
    path('event/<int:pk>/delete/', views.delete_workout, name="delete_workout"),
    path('progress/', views.progress, name="goals")
    # path('routines/<int:pk>/schedule', views.workout_shortcut, name='routine_schedule')
]




