from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RoutineForm, WorkoutForm, ExerciseForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from .models import Routine, Exercise, Workout

@login_required(login_url='/login/')
def index(request):
    routines = Routine.objects.filter(user_id=request.user.id)
    return render(request, 'workout/index.html', {'routines': routines})

@login_required(login_url='/login/')
def routine_create(request):
    if request.method == 'POST':
        form = RoutineForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            routine = form.save()
            return redirect('workout')
    else: 
        form = RoutineForm()
    context = {'form': form, 'header': 'Add a new workout routine'}
    return render(request, 'workout/routine_form.html', context)

@login_required(login_url='/login/')
def routine_edit(request, pk):
    routine = Routine.objects.get(pk=pk)
    if routine.user_id == request.user.id:

        if request.method == 'POST':
            form = RoutineForm(request.POST, instance=routine)
            if form.is_valid():
                routine = form.save()
                return redirect('workout')
        else: 
            form = RoutineForm(instance=routine)
        
        return render(request, 'workout/routine_form.html', {'form':form})
    else: 
        return redirect('workout')


@login_required(login_url='/login/')
def routine_delete(request, pk):
    routine = Routine.objects.get(pk=pk)
    if routine.user_id == request.user.id:
        routine.delete()
    return redirect('workout')