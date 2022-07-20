from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RoutineForm, WorkoutForm
from datetime import datetime, timedelta, date
from django.forms import inlineformset_factory
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django import forms

from django.utils.safestring import mark_safe
import calendar
# from utils import Calendar
# Create your views here.
from django.http import HttpResponse
from .models import *

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
    if routine.user.id != request.user.id:
            return redirect('workout')
    context = {
        'routine': routine
    }
    return render(request, 'workout/routine.html', context)




@login_required(login_url='/login/')
def routine_edit(request, pk):
    routine = Routine.objects.get(pk=pk)
    if routine.user_id == request.user.id:
        ExerciseFormset = inlineformset_factory(Routine, Exercise, fields =('name', 'time', 'weight','reps', 'sets', 'distance', 'notes'), extra=1)
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




## calendar 

# class CalendarView(ListView):
#     model = Workout
#     template_name = 'components/calendar.html'
#     success_url = reverse_lazy("calendar")
# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     d = get_date(self.request.GET.get('month', None))
#     cal = Calendar(d.year, d.month)
#     html_cal = cal.formatmonth(withyear=True)
#     context['calendar'] = mark_safe(html_cal)
#     context['prev_month'] = prev_month(d)
#     context['next_month'] = next_month(d)
    
#     return context



from .utils import Calendar

class CalendarView(generic.ListView):
    model = Workout
    template_name = 'workout/schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))
        

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table

        html_cal = cal.formatmonth(withyear=True, user=self.request.user)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

@login_required(login_url='/login/')
def workout(request, pk=None):
    instance = Workout()
    if pk:
        instance = get_object_or_404(Workout, pk=pk)
        # validate that the user has permission to edit this Workout
        if instance.user.id != request.user.id:
            return redirect('calendar')
    else: 
        instance = Workout()
    form = WorkoutForm(request.POST or None, instance=instance)
    form.fields['routine'] = forms.ModelChoiceField(Routine.objects.filter(user__id = request.user.id))
    form.instance.user = request.user
    if request.POST and form.is_valid():
        form.save()
        return redirect('calendar')
    return render(request, 'workout/event.html', {'form': form})