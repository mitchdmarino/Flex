from django import forms 

from .models import Workout, Routine, Exercise

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'type', 'details', 'public']
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'type', 'details', 'public']
class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'type', 'details', 'public']