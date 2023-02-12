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

class GoodsForm(forms.ModelForm):
     class Meta:
        model = Goods
        fields = ('g_category', 'gid', 'g_name', 'brand', 'price', 'Net', 'product')
        widgets = {
                'g_category': forms.Select(attrs={'class': 'form-control'}),
                'gid': forms.TextInput(attrs={'class': 'form-control'}),
                'g_name': forms.TextInput(attrs={'class': 'form-control'}),
                'brand': forms.TextInput(attrs={'class': 'form-control'}),
                'g_models': forms.TextInput(attrs={'class': 'form-control'}),
                'price': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
                'Net': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
                'product': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 60}),
            }
        labels = {
                'g_category': 'Goodscategory',
                'gid': 'Goodsid',
                'g_name': 'Goodsname',
                'brand': 'Brand',
                'g_models': 'Models',
                'price': 'Price',
                'net': 'Net',
                'product': 'Property',

        }

class GoodsFormUpdate(forms.ModelForm):
    class Meta:
            model = Goods
            fields = ('g_category', 'gid', 'g_name', 'brand', 'price', 'Net', 'product')
            widgets = {
                'g_category': forms.Select(attrs={'class': 'form-control'}),
                'gid': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
                'g_name': forms.TextInput(attrs={'class': 'form-control'}),
                'brand': forms.TextInput(attrs={'class': 'form-control'}),
                'g_models': forms.TextInput(attrs={'class': 'form-control'}),
                'price': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
                'Net': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
                'product': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 60}),
            }
            labels = {
                'g_category': 'Goodscategory',
                'gid': 'Goodsid',
                'g_name': 'Goodsname',
                'brand': 'Brand',
                'g_models': 'Models',
                'price': 'Price',
                'net': 'Net',
                'product': 'Property',

            }

class CusForm(forms.ModelForm):
        class Meta:
            model = Customer
            fields = ('cid', 'name', 'surname', 'address', 'tel', 'gender', 'carreer', 'password')
            CHOICES = [('M', 'Male'), ('F', 'Female')]
            widgets = {
                'cid': forms.TextInput(attrs={'class': 'form-control'}),
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'surname': forms.TextInput(attrs={'class': 'form-control'}),
                'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 60}),
                'tel': forms.TextInput(attrs={'class': 'form-control'}),
                'gender': forms.RadioSelect(choices=CHOICES),
                'carreer': forms.TextInput(attrs={'class': 'form-control'}),
                'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            }
            labels = {
                'cid': 'Cid',
                'name': 'name',
                'surname': 'surname',
                'address': 'address',
                'tel': 'Tel',
                'gender': 'gender',
                'carreer': 'carreer',
                'password': 'password'
            }

class CusFormUpdate(forms.ModelForm):
        class Meta:
            model = Customer
            fields = ('cid', 'name', 'surname', 'address', 'tel', 'gender', 'carreer', 'password')
            CHOICES = [('M', 'Male'), ('F', 'Female')]
            widgets = {
                'cid': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'surname': forms.TextInput(attrs={'class': 'form-control'}),
                'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 60}),
                'tel': forms.TextInput(attrs={'class': 'form-control'}),
                'gender': forms.RadioSelect(choices=CHOICES),
                'carreer': forms.TextInput(attrs={'class': 'form-control'}),
                'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            }
            labels = {
                'cid': 'Cid',
                'name': 'name',
                'surname': 'surname',
                'address': 'address',
                'tel': 'Tel',
                'gender': 'gender',
                'carreer': 'carreer',
                'password': 'password'
            }
