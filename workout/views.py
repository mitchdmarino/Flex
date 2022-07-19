from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RoutineForm, WorkoutForm

from django.forms import inlineformset_factory

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

def routine_details(request, pk):
    routine = Routine.objects.get(pk=pk)
    context = {
        'routine': routine
    }
    return render(request, 'workout/routine.html', context)




@login_required(login_url='/login/')
def routine_edit(request, pk):
    routine = Routine.objects.get(pk=pk)
    if routine.user_id == request.user.id:
        ExerciseFormset = inlineformset_factory(Routine, Exercise, fields =('name', 'time', 'reps', 'sets', 'distance', 'notes'), extra=1)
        if request.method == 'POST':
            form = RoutineForm(request.POST, instance=routine)
            formset = ExerciseFormset(request.POST, instance=routine)
            if formset.is_valid() and form.is_valid():
                formset.save()
                form.save()
                return redirect("/workout/routines/" + str(pk))
        else: 
            form = RoutineForm(instance=routine)
            formset = ExerciseFormset(instance=routine)
        return render(request, 'workout/routine_form.html', {'routine':routine,'form':form, 'exerciseForm':formset})
    else: 
        return redirect("/workout/routines/" + str(pk))


@login_required(login_url='/login/')
def routine_delete(request, pk):
    routine = Routine.objects.get(pk=pk)
    if routine.user_id == request.user.id:
        routine.delete()
    return redirect('workout')