from django.shortcuts import render

def main(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
