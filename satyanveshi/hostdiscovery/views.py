from django.shortcuts import render, HttpResponse

def hostdiscovery(request):
    return render(request,'hostdiscovery.html')
