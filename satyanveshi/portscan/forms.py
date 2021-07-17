from django import forms

class scanport(forms.Form):
    ip = forms.CharField(label='ip', max_length=100)