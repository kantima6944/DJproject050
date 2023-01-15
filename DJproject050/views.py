from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def myinfo (request):
    return render(request,'myinfo.html')
def education (request):
    return render(request,'education.html')
def interest (request):
    return render(request,'interest.html')
def sales (request):
    return render(request,'sales.html')
def rloe (request):
    return render(request,'rloe.html')
def etc(request):
    return render(request,'etc.html')
