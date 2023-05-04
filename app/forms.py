from django import forms

class myform(forms.Form):
    question = forms.CharField(max_length=150, required=False)
    answer = forms.CharField(max_length=50, required=False)
    result = forms.CharField(max_length=50, required=False)
