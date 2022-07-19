from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RoutineForm, WorkoutForm

from django.forms import inlineformset_factory

from django.contrib.auth.decorators import login_required

# from utils import Calendar
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
def schedule(request):
    return HttpResponse('hello')
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar

class CalendarView(generic.ListView):
    model = Workout
    template_name = 'workout/schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True, user=self.request.user)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()