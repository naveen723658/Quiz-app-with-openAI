from django.shortcuts import render
from . forms import myform
def signup(request):
    fm = myform()
    return render(request, "signup.html" , {"myform":fm})

def login(request):
    return render(request, "login.html" )
