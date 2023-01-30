from django.forms import *

from .models import *
class ProductMFrom(forms.ModelForm):

    id = forms.CharField( max_length = 13 , lable = "รหัสสินค้า",
                          required = True , widget=forms.TextInput(attrs={'size': '15'}))
    name = forms.CharField(max_length=50, lable="ชื่อสินค้า",
                         required=True, widget=forms.TextInput(attrs={'size': '55'}))
    brand = forms.CharField(max_length=30, lable="ยี่ห้อ",
                         required=True, widget=forms.TextInput(attrs={'size': '35'}))
    price = forms.CharField(min_value=1.00, max_length=1000000.00, lable="ราคาต่อหน่วย",
                         required=True, widget=forms.NumberInput(attrs={'size': '10'}))
    id = forms.CharField(min_value=0,max_length=1000, lable="คงเหลือ",
                         required=True, widget=forms.NumberInput(attrs={'size': '10'}))

    class Meta:
        model = Product
        fields = ('pid','name','brand','price','net','category')
        Widget={
            'pid':forms.TextInput(attrs={'class':'form-contrpl'}),
            'name': forms.TextInput(attrs={'class': 'form-contrpl' }),
            'brand': forms.TextInput(attrs={'class': 'form-contrpl'}),
            'price': forms.TextInput(attrs={'class': 'form-contrpl'}),
            'net': forms.TextInput(attrs={'class': 'form-contrpl'}),
            'category': forms.TextInput(attrs={'class': 'form-contrpl'}),
        }
        labels = {
            'pid':'รหัสสินค้า' , 'name':'ชื่อสินค้า' , 'brand': 'ยี่ห้อ' , 'price':'ราคาต่อหน่วย' ,
            'net':'คงเหลือ' , 'category':'ประเภทสินค้า'
        }
