
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import DonHangForm, KhachMuaForm
from .models.khach_hang import KhachMua
from .models.san_pham import LoaiSanPham, Mo


def get_all_mo_in_grouped_objects():
    all_mo = Mo.objects.all()

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


def order(request, customer_id=None):
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
                return redirect("existing_customer_order")  # Redirect to the same page to avoid resubmitting the form
        else:
            # Handle creating a new customer and order
            khach_mua_form = KhachMuaForm(request.POST, prefix="khachhang")
            donhang_form = DonHangForm(request.POST, prefix="donhang")

            if khach_mua_form.is_valid() and donhang_form.is_valid():
                khachhang = khach_mua_form.save()
                donhang = donhang_form.save(commit=False)
                donhang.khach_mua = khachhang
                donhang.save()
                return redirect("new_customer_order")  # Redirect to the same page to avoid resubmitting the form
    else:
        khach_mua_form = KhachMuaForm(prefix="khachhang")
        donhang_form = DonHangForm(prefix="donhang")

    customers = KhachMua.objects.all()
    return render(request, "dat_hang.html", {"khach_mua_form": khach_mua_form, "donhang_form": donhang_form, "customers": customers})
