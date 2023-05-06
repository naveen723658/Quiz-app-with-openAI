from django import forms

class myform(forms.Form):
    question = forms.CharField(max_length=150, required=False)
    answer = forms.CharField(max_length=50, required=False)
    result = forms.CharField(max_length=50, required=False)

class signup(forms.Form):
    fname = forms.CharField(max_length=10, required=False)
    lname = forms.CharField(max_length=10, required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(max_length=10, required=False)

class signin(forms.Form):
    email = forms.EmailField(
        label = "Email address",
        widget = forms.EmailInput,
        required = True,
    )
    password = forms.CharField(max_length=10, required=False)
