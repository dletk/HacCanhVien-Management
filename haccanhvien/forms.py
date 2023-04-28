from django.forms import ModelForm, widgets

from .models.khach_hang import KhachMat, KhachMua
from .models.sales import DonHang


class KhachMuaForm(ModelForm):
    class Meta:
        model = KhachMua
        fields = '__all__'


class KhachMatForm(ModelForm):
    class Meta:
        model = KhachMat
        fields = "__all__"
        exclude = ["mo"]
        widgets = {
            "ngay_mat": widgets.DateInput(attrs={"type": "date"}),
            "ten_khach": widgets.TextInput(attrs={"class": "form-control"}),
            "thong_tin_khac": widgets.Textarea(attrs={"class": "form-control"}),
        }
class DonHangForm(ModelForm):
    class Meta:
        model = DonHang
        exclude = ["khach_mua"]
        widgets = {
            "ngay_giao_dich": widgets.DateInput(attrs={"type": "date"})
        }
