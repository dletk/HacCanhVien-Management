
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import DonHangForm, KhachMatForm, KhachMuaForm
from .models.khach_hang import KhachMua
from .models.sales import DonHang
from .models.san_pham import LoaiSanPham, Mo


def get_all_mo_in_grouped_objects(filter_dict=None):
    if filter_dict is None:
        filter_dict = {}
    all_mo = Mo.objects.filter(**filter_dict)

    grouped_objects = []

    for obj in all_mo:
        grouped_objects.append((obj.hang, obj.cot, obj))

    context = {"grouped_objects": grouped_objects}
    return context

# Create your views here.


def index(request):
    return HttpResponse("Hello, world! Small step towards a big system!")


def ban_hang(request):
    context = get_all_mo_in_grouped_objects()

    all_ma_san_pham = LoaiSanPham.objects.all()
    context["all_ma_san_pham"] = all_ma_san_pham

    return render(request, "thong_tin_du_an.html", context)


def order(request, customer_id=None, mo_id=None):
    if request.method == "POST":
        if customer_id:
            # Handle creating a new order for the existing customer
            khach_mua = KhachMua.objects.get(pk=customer_id)
            donhang_form = DonHangForm(request.POST, prefix="donhang")
            if donhang_form.is_valid():
                donhang = donhang_form.save(commit=False)
                donhang.khach_mua = khach_mua
                donhang.save()
                danh_sach_dich_vu = donhang_form.cleaned_data["danh_sach_dich_vu"]
                donhang.danh_sach_dich_vu.set(danh_sach_dich_vu)
                return redirect("order")  # Redirect to the same page to avoid resubmitting the form
        else:
            # Handle creating a new customer and order
            khach_mua_form = KhachMuaForm(request.POST, prefix="khachhang")
            donhang_form = DonHangForm(request.POST, prefix="donhang")

            if khach_mua_form.is_valid() and donhang_form.is_valid():
                khachhang = khach_mua_form.save()
                donhang = donhang_form.save(commit=False)
                donhang.khach_mua = khachhang
                donhang.save()
                danh_sach_dich_vu = donhang_form.cleaned_data["danh_sach_dich_vu"]
                donhang.danh_sach_dich_vu.set(danh_sach_dich_vu)
                return redirect("order")  # Redirect to the same page to avoid resubmitting the form
    else:
        khach_mua_form = KhachMuaForm(prefix="khachhang")
        donhang_form = DonHangForm(prefix="donhang")

    customers = KhachMua.objects.all()
    return render(request, "dat_hang.html", {"khach_mua_form": khach_mua_form, "donhang_form": donhang_form, "customers": customers})

@require_http_methods(["GET", "POST"])
def quan_li_don_hang(request, ma_don_hang=None, trang_thai=None):
    if request.method == "GET":
        context = get_all_mo_in_grouped_objects()
        context["all_don_hang"] = {
            "don_hang_dang_giao_dich": DonHang.objects.filter(trang_thai=DonHang.DANG_CHO),
            "don_hang_da_hoan_tat": DonHang.objects.filter(trang_thai=DonHang.HOAN_TAT)
        }
        return render(request, "quan_li_don_hang.html", context)
    elif request.method == "POST":
        if ma_don_hang and trang_thai:
            don_hang = DonHang.objects.get(ma_don_hang=ma_don_hang)
            valid_trang_thai = [choice[0] for choice in DonHang.TRANG_THAI]

            if trang_thai not in valid_trang_thai:
                return f"Error, cannot set trang thai of Don hang to {trang_thai}"

            don_hang.trang_thai = trang_thai
            don_hang.save()

            return redirect("quan_li_don_hang")

@require_http_methods(["GET", "POST"])
def add_nguoi_mat(request, moid: int):
    if request.method == "GET":
        khach_mat_form = KhachMatForm()
        return render(request, "thong_tin_nguoi_mat.html", {"khach_mat_form": khach_mat_form})
    else:
        khach_mat_form = KhachMatForm(request.POST)
        if khach_mat_form.is_valid():
            mo = Mo.objects.get(pk=moid)
            khach_mat = khach_mat_form.save(commit=False)
            khach_mat.mo = mo
            khach_mat.save()
            return redirect("so-do-du-an")
