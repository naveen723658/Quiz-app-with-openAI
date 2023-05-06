from django.shortcuts import render
from django.contrib.auth.models import User
from . forms import *
from django.http import JsonResponse
def signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,email=email, password=password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        print(f"fname = {fname}, lname = {lname}, email = {email}, password = {password}")
        return JsonResponse({'message': 'User created successfully'})
    return render(request, "signup.html" )

def login(request): 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"email = {email} , password = {password}")    
    return render(request, "login.html" )
