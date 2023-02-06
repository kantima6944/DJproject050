from django.shortcuts import render, redirect
from ProfileApp.models import *
from ProfileApp.forms import *
import datetime
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

def mydata(request):
    name = "นางสาวกัณทิมา ยุซิ"
    stdid = "65342310050-2"
    address = "92 ม.7 ต.โนนแดง อ.โนนศิลา จ.ขอนแก่น รหัสไปรษณีย์ 40110"
    gender = "หญิง"
    weigth = "43"
    heigth = "165"
    colors = "สีชมพู,แดง"
    food = "อาหารประเภทตำ,ปิ้งย่าง"
    job = "นักศึกษา"

    myproduct = [["ซันซิล สูตรฟื้นฟูโครงสร้างผมแห้งเสีย", "99", "images/su3.jpg"],
                 ["ซันซิล สูตรผมตรงสวยสมบูรณ์แบบ", "79", "images/su1.jpg"],
                 ["ซันซิล ช่วยบำรุงผมที่ยาวให้มีสุขภาพดี", "109", "images/su7.jpg"],
                 ["ซันซิล ช่วยบำรุงเส้นผม ให้ผมรู้สึกชุ่มชื้น", "299", "images/su5.jpg"],
                 ["ซันซิล สูตรปกป้องเส้นผมจากสภาพอากาศ ", "399", "images/su6.jpg"],
                 ]
    return render(request, 'showmydata.html', {'name':name, 'stdid':stdid, 'address':address, 'gender':gender,
                                          'weigth':weigth, 'heigth':heigth, 'colors':colors, 'food':food,
                                          'job':job, 'myproduct':myproduct})

lstOurProduct = []
def listProduct(request):
    details = "ยาสระผม"
    name = "นางสาวกัณทิมา ยุซิ"
    date = datetime.datetime.now()
    return render(request, 'listProduct.html', {'lstProduct': lstOurProduct,
                                              'details': details, 'name': name,
                                              'date': date.strftime("%A %d-%m-%Y %H : %M")})
def inputProduct(request):
    if request.method == 'POST':
        form = ProductFrom(request.POST)
        if form.is_valid():
            pid = form.cleaned_data['pid']
            pname = form.cleaned_data['name']
            brand = form.cleaned_data['brand']
            price = form.cleaned_data['price']
            am = form.cleaned_data['amount']
            promotion = form.cleaned_data['promotion']
            productnew = Productlab11(pid, pname,  brand, price, am, promotion)
            lstOurProduct.append(productnew)
            return redirect('listProduct')
        else:
            return redirect('pro_retrive_all')
    else:
        form = ProductFrom()
    context = {
        'form': form
    }
    return render(request, 'inputProduct.html', context)






#def updateProduct(request,pid):
    #product = get_object_or_404(Product,pid=pid)
    #from = ProductFrom(data=request.POST or None,instance=product)
    #if


