import pytest

from django.contrib.auth.models import User
from workout.models import Routine, Workout, Exercise

@pytest.fixture()
def new_user_factory(db):
    def create_app_user(username: str,
        password: str = None,
        first_name: str = "fistname",
        last_name: str = "lastname",
        email: str = 'test@test.com',
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name = first_name,
            last_name = last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user
    return create_app_user

@pytest.fixture()
def new_user1(db, new_user_factory):
    print('making user1')
    return new_user_factory("User1", "password", "ONE")
# @pytest.fixture
# def new_user2(db, new_user_factory):
#     print('making user2')
#     return new_user_factory("User2", "password", "TWO")

# ## ROUTINE FACTORY
# @pytest.fixture()
# def new_routine_factory(db):
#     def create_routine(
#         name: str,
#         type: str = 'Cardio',
#         user: 
#     ):
#         user = User.objects.create_user(
#             username=username,
#             password=password,
#             first_name = first_name,
#             last_name = last_name,
#             email=email,
#             is_staff=is_staff,
#             is_superuser=is_superuser,
#             is_active=is_active,
#         )
#         return user
#     return create_app_user

# @pytest.fixture
# def new_user1(db, new_user_factory):
#     return new_user_factory("User1", "password", "ONE")