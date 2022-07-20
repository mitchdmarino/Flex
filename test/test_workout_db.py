import pytest

from django.contrib.auth.models import User
from workout.models import Routine, Workout, Exercise

# user created
def test_new_user(new_user1):
    print(new_user1.first_name)
    assert new_user1.first_name == 'ONE'

# test adding a routine to a user
def test_add_routine(new_user1):
    new_user1.routine_set.create(name="Leg Day", type = 'Strength')
    routine = new_user1.routine_set.filter(name="Leg Day", type = 'Strength')
    print(routine)
    assert routine

# test deleting a routine 
def test_delete_routine(new_user1):
    new_user1.routine_set.create(name="5k run", type= 'Cardio')
    routine = new_user1.routine_set.filter(name="5k run")
    routine.delete()
    assert not new_user1.routine_set.filter(name="5k run")

# test editing a user's routine
def test_edit_routine(new_user1):
    new_user1.routine_set.create(name="5k run", type= 'Cardio')
    routine = new_user1.routine_set.get(name="5k run")
    routine.name = "10k run"
    routine.save()    
    assert new_user1.routine_set.get(name="10k run")
    

# test adding exerces to a user's routine

def test_add_exercise(new_user1):
    new_user1.routine_set.create(name="5k run", type= 'Cardio')
    routine = new_user1.routine_set.get(name="5k run")
    exercice = Exercise.objects.create(name="run 5 kilometers", time="10:00", distance="5000", routine=routine)
    exercise = Exercise.objects.get(name="run 5 kilometers")
    assert exercise.routine.id == routine.id


# test scheduling a workout from a routine 

def test_schedule_workout(new_user1):
    new_user1.routine_set.create(name="5k run", type= 'Cardio')
    routine = new_user1.routine_set.get(name="5k run")
    activity = Workout.objects.create(user=new_user1, routine = routine, day="2022-07-07", start_time="12:26:00")
    assert activity.routine.id == routine.id


# test completing a workout 

def test_complete_workout(new_user1):
    new_user1.routine_set.create(name="5k run", type= 'Cardio')
    routine = new_user1.routine_set.get(name="5k run")
    activity = Workout.objects.create(user=new_user1, routine = routine, day="2022-07-07", start_time="12:26:00")
    activity.complete = True
    assert activity.complete

