from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Routine(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=10,
        choices=[
            ('Cardio', 'Cardio'),
            ('Strength', 'Strength'),
        ],
        default='Strength'
    )
    details = models.CharField(max_length=250)
    public = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
        return self.name
    

# Workout class, is used to schedule a routine for a specific time
class Workout(models.Model):
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    routine = models.ForeignKey('Routine', on_delete=models.CASCADE, related_name='routine')
    notes = models.TextField(u'Textual Notes', help_text=u'Notes', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    @property
    def get_html_url(self):
        url = reverse('edit_workout', args=(self.id,))
        return f'<a href="{url}"> {self.routine.name} </a>'
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'
    
    


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField(blank=True, default=0)
    sets = models.IntegerField(blank=True ,default=0)
    reps = models.IntegerField(blank=True ,default=0)
    distance = models.IntegerField(blank=True ,default=0)
    time = models.TextField(blank=True, null=True)
    notes = models.CharField(max_length=250, default='')
    routine = models.ForeignKey('Routine', on_delete=models.CASCADE, related_name='exercises')

    def __str__(self): 
        return self.name
