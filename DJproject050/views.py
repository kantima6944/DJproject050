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
    details = "โทรศัพท์มือถือ"
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
def showGoodsList (request):
    #Query
    result = Goods.objects.all()
    return render(request, 'showGoodsList.html', {'result' : result})

def showGoodsOne (request,gid):
    context ={}
    goodsone_info = Goods.objects.get(gid=gid)
    #result ={'goodsone_info':goodsone_info}
    form = GoodsForm(request.POST or None, instance=goodsone_info)
    context["form"] = form
    return render(request, 'showGoodsOne.html', context)



def newGoodsCreate (request):
    context = {}
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        obj = Goods.objects.filter(gid=request.POST['gid'])
        if obj:
            context["form"] = form
            return render(request, "newGoodsCreate.html", context)
        if form.is_valid():
            form.save()
            return redirect('goodslist')
        else:
            return redirect('pro_retrive_all')
    else:
        form = GoodsForm()
    context = {
        'form': form
    }
    return render(request, 'newGoodsCreate.html', context)
def GoodsUpdate (request,gid):
    context = {}
    obj = Goods.objects.get(gid=gid)
    form = GoodsFormUpdate(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('goodslist')
    else:
        context["form"] = form
        return render(request, "GoodsUpdate.html", context)

def GoodsDel (request,gid):
    goods = Goods.objects.get(gid=gid)
    if request.method =="GET":
        goods.delete()
        return redirect('goodslist')
    # value = {'value': goods}
    # return render(request, 'form/Goodsdel.html', value)

def showCustomerList (request):
    result = Customer.objects.all()
    return render(request, 'showCustomerList.html', {'result': result})

def register (request):
    context = {}
    if request.method == 'POST':
        form = CusForm(request.POST)
        obj = Customer.objects.filter(cid=request.POST['cid'])
        if obj:
            context["form"] = form
            return render(request, "newGoodsCreate.html", context)
        if form.is_valid():
            form.save()
            return redirect('customerList')
        else:
            return redirect('pro_retrive_all')
    else:
        form = CusForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def CustomerUpdate (request,cid):
    context = {}
    obj = Customer.objects.get(cid=cid)
    form = CusFormUpdate(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('customerList')
    else:
        context["form"] = form
        return render(request, "CustomerUpdate.html", context)

def CustomerDel (request,cid):
    Cus = Customer.objects.get(cid=cid)
    if request.method == "GET":
        Cus.delete()
        return redirect('customerList')
    # value = {'value':Cus}
    # return render(request,'form/showCustomerList.html',value)

def showCusOne (request,cid):
    context ={}
    Cusone_info = Customer.objects.get(cid=cid)
    #result ={'goodsone_info':goodsone_info}
    form = CusForm(request.POST or None, instance=Cusone_info)
    context["form"] = form
    return render(request, 'showCusOne.html', context)






#def updateProduct(request,pid):
    #product = get_object_or_404(Product,pid=pid)
    #from = ProductFrom(data=request.POST or None,instance=product)
    #if


