from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Routine, Exercise, Workout

def index(request):
    routines = Routine.objects.all()
    print(routines)
    exercises = routines[0].exercises.all()
    return render(request, 'workout/index.html', {'routines': routines, 'exercises':exercises })