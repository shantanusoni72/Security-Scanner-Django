from django.shortcuts import render
#from portscanner import *
from .forms import *

def scanning(request):
    if request.method == 'POST':
        form = scanport(request.POST)
        if form.is_valid():
            print('It works')
    return render(request, 'portscan.html')
