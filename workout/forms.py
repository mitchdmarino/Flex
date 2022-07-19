from django import forms


from .models import Workout, Routine, Exercise

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'type', 'details', 'public']

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
            'end_time': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
        }
        fields = ['day','start_time', 'end_time' ,'routine', 'notes']


    def __init__(self, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%H:%M',)
        self.fields['end_time'].input_formats = ('%H:%M',)
