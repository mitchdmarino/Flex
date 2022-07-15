from django.contrib import admin

# Register your models here.
from .models import Routine, Workout, Exercise

admin.site.register(Routine)
admin.site.register(Workout)
admin.site.register(Exercise)