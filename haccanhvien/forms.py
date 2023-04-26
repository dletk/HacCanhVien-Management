from django.forms import ModelForm, widgets

from .models.khach_hang import KhachMua
from .models.sales import DonHang


class KhachMuaForm(ModelForm):
    class Meta:
        model = KhachMua
        fields = '__all__'


class DonHangForm(ModelForm):
    class Meta:
        model = DonHang
        exclude = ["khach_mua"]
        widgets = {
            "ngay_giao_dich": widgets.DateInput(attrs={"type": "date"})
        }
