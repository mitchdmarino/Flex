import factory

# get fake data easily
from faker import Faker
fake = Faker()

from django.contrib.auth.models import User
from workout.models import Workout, Routine, Exercise

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = fake.name()

class RoutineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Routine
    name = fake.company()
    type = 'Cardio'
    user = User #

# def test_1():
#     assert 1==1