from django.shortcuts import render
from django.contrib.auth.models import User
from . forms import *
from django.http import JsonResponse
from django.core.mail import send_mail
import math, random
import json

def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP


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
        htmlgen = '<p>Your OTP is <strong>code</strong></p>'
        send_mail('OTP request',[email], fail_silently=False, html_message=htmlgen)
        return JsonResponse({'message': 'User created successfully'})
    return render(request, "signup.html" )

def login(request): 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"email = {email} , password = {password}")    
    return render(request, "login.html" )
