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
def showMyData(request):
    name = "kantima"
    surname="yusi"
    gender="Male"
    status="Lecturer"
    work="RMUTI Khonkean"
    education= "Ph.D.Information Studies"
    return request(request,'showMyData.html'),
    {'name':name, 'surname':surname,'gener':gener ,'status': status, 'work':work,"education":education}







