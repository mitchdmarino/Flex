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
    



@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()
