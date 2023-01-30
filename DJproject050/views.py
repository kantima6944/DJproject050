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


