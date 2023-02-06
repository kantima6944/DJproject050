from django import forms
from .models import *
class ProductFrom(forms.Form):
    choicePro = (('มี','มี'), ('ไม่มี','ไม่มี'))
    pid = forms.CharField(label = "รหัสสินค้า",)
    name = forms.CharField(max_length=50, label="ชื่อสินค้า",
                         required=True, widget=forms.TextInput(attrs={'size': '55'}))
    brand = forms.CharField(max_length=30, label="ยี่ห้อ",
                         required=True, widget=forms.TextInput(attrs={'size': '35'}))
    price = forms.IntegerField(label="ราคา")
    amount = forms.IntegerField(min_value=0, label="คงเหลือ")
    promotion = forms.CharField(label= "โปรโมชั่น",widget=forms.Select(choices= choicePro))
