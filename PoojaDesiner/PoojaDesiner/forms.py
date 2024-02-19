from django import forms

class Djangoform(forms.Form):

    num1 = forms.CharField(label='Value1',required=True,widget=forms.TextInput(attrs={"class": "form-control"}))
    num2 = forms.CharField(label='Value2',required=True,widget=forms.TextInput(attrs={"class": "form-control"}))

    
