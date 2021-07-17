from django import forms

class spidering(forms.Form):
    host = forms.CharField(label='host', max_length=100)