from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Routine(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=10,
        choices=[
            ('Cardio', 'Cardio'),
            ('Strength', 'Strength'),
        ]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
        return self.name
    

# Workout class, is used to schedule a routine for a specific time
class Workout(models.Model):
    date = models.DateField()
    completed = models.BooleanField(default=False)    
    routine = models.ForeignKey('Routine',on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    routine = models.ForeignKey('Routine', on_delete=models.CASCADE, related_name='exercises')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

