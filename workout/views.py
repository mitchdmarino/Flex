from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Routine

def index(request):
    print("ROUTINES", Routine.objects.all())
    return HttpResponse('<h1>Your workout routines</h1>')