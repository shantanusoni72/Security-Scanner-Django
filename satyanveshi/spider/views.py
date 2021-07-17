from django.shortcuts import render
from spider import views
from .forms import *
#from crawler import *

def spider(request):
    if request.method == 'POST':
        form = spidering(request.POST)
        if form.is_valid():
            print('Works')
    return render(request, 'spider.html')
