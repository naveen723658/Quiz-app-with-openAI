from django.shortcuts import render
from django.contrib.auth.models import User
from . forms import *
from django.http import JsonResponse
import json
def signup(request):
    if request.method == "POST":
        data = json.loads(request.body)
        fname = data.get('fname')
        lname = data.get('lname')
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        user = User.objects.create_user(username=username,email=email, password=password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return JsonResponse({'message': 'User created successfully'})
    return render(request, "signup.html" )

def login(request): 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"email = {email} , password = {password}")    
    return render(request, "login.html" )
