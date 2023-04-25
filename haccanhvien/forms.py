from django import forms

from .models.khach_hang import KhachMua
from .models.sales import DonHang


class KhachMuaForm(forms.ModelForm):
    class Meta:
        model = KhachMua
        fields = '__all__'


class DonHangForm(forms.ModelForm):
    class Meta:
        model = DonHang
        exclude = ["khach_mua"]
