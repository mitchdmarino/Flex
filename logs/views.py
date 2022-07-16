from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


# Create your views here.
def login_page(request):
    return render(request, 'login_form.html')

# add after 'login_page'
def profile_show(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return render(request, 'profile.html')
    else:
        return HttpResponse('<h1>Something went wrong with login</h1>')