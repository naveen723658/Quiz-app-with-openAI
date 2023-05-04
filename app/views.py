from django.shortcuts import render
from . forms import myform
def home(request):
    fm = myform()
    return render(request, "index.html" , {"myform":fm})
