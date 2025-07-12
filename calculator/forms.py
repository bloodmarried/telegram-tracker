from django import forms

class NumberTon(forms.Form):
    
    ton = forms.IntegerField()