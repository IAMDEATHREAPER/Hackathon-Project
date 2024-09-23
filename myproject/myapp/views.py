from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Features
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def selection(request):
    bulk = request.GET['bulk']
    return render(request, 'selection.html', {'bulk':bulk})

def input(request):
    return render(request, 'ginput.html')

def tracker(request):
    return render(request, 'tracker.html')

def output(request):
    weight = request.POST['weight']
    height = request.POST['height']
    age = request.POST['age']
    gender = request.POST['gender']
    if gender == 'male':
        bmr = 10*int(weight) + 6.25*int(height) - 5*int(age) + 5
    else:
        bmr = 10*int(weight) + 6.25*int(height) -5*int(age) -161 
    return render(request, 'Output.html', {'bmr' : bmr})
'''
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username alredy exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html') 
    
def login(request):
    return render(request, 'login.html')
'''

def about(request):
    return render(request, 'newabout.html')

def contact(request):
    return render(request, 'fancycontact.html')