from django import forms 
from django.forms import inlineformset_factory

from .models import Workout, Routine, Exercise

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'type', 'details', 'public']
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date']



        

