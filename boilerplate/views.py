from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_page(request):
    return render(request, 'login_form.html')

# add after 'login_page'
def profile_show(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    else: 
        user = request.user
    if user is not None:
        login(request,user)
        return render(request, 'profile.html')
    else:
        return HttpResponse('<h1>Something went wrong with login</h1>')



def logout_view(request):
    logout(request)
    return redirect('workout')


from .form import SignUpForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user = authenticate(username=user.username, password=user.password)
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('profile')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})