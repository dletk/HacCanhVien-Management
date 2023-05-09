
from collections import defaultdict
from datetime import datetime

from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import DonHangForm, KhachMatForm, KhachMuaForm
from .models.dich_vu import DichVu
from .models.khach_hang import AnhKyUc, KhachMat, KhachMua, KyUc
from .models.sales import DonHang, GiayChungNhan
from .models.san_pham import LoaiSanPham, Mo, TinhTrangMo


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


def dat_hang(request, customer_id=None, mo_id=None):
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
    all_dich_vu = DichVu.objects.all()
    return render(request, "dat_hang.html", {"khach_mua_form": khach_mua_form, "donhang_form": donhang_form, "customers": customers, "all_dich_vu": all_dich_vu})


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
        khach_mat_form = KhachMatForm(prefix="khachmat")
        return render(request, "them_thong_tin_nguoi_mat.html", {"khach_mat_form": khach_mat_form})
    else:
        khach_mat_form = KhachMatForm(request.POST, prefix="khachmat")
        if khach_mat_form.is_valid():
            mo = Mo.objects.get(pk=moid)
            khach_mat = khach_mat_form.save(commit=False)
            khach_mat.mo = mo
            khach_mat.save()

            if "file-upload" in request.FILES:
                ky_uc = KyUc(khach_hang=khach_mat)
                ky_uc.save()
                files = request.FILES.getlist('file-upload')
                for f in files:
                    # Save the uploaded file
                    img = SimpleUploadedFile(f.name, f.read())
                    anh_ky_uc = AnhKyUc(ma_ky_uc=ky_uc, image=img)
                    anh_ky_uc.save()

            return redirect("so-do-du-an")


@require_http_methods(["GET"])
def thong_tin_nguoi_mat(request, moid: int):
    context = {}
    mo = Mo.objects.get(pk=moid)
    cac_khach_mat = KhachMat.objects.filter(mo=mo)

    context["cac_khach_mat"] = cac_khach_mat
    context["mo"] = mo
    return render(request, "thong_tin_nguoi_mat.html", context)


@require_http_methods(["GET", "POST"])
def quan_li_giay_chung_nhan(request, giay_chung_nhan_id=None, trang_thai=None):
    if request.method == "GET":
        context = get_all_mo_in_grouped_objects()
        context["all_giay_chung_nhan"] = {
            "giay_chung_nhan_dang_cho": GiayChungNhan.objects.filter(trang_thai=GiayChungNhan.DANG_CHO),
            "giay_chung_nhan_da_hoan_tat": GiayChungNhan.objects.filter(trang_thai=GiayChungNhan.HOAN_TAT)
        }
        return render(request, "giay_chung_nhan.html", context)
    elif request.method == "POST":
        if giay_chung_nhan_id and trang_thai:
            giay_chung_nhan = GiayChungNhan.objects.get(pk=giay_chung_nhan_id)
            valid_trang_thai = [choice[0] for choice in GiayChungNhan.TRANG_THAI]

            if trang_thai not in valid_trang_thai:
                return f"Error, cannot set trang thai of Don hang to {trang_thai}"

            giay_chung_nhan.trang_thai = trang_thai
            giay_chung_nhan.save()

            # If trang thai change to DANG_CHO, the associated Mo should be marked as Dang Giao Dich, not Da Ban
            mo = giay_chung_nhan.don_hang.mo
            if trang_thai == "DANG_CHO" and mo.tinh_trang_mo == TinhTrangMo.objects.get(ma_tinh_trang="DB"):
                mo.tinh_trang_mo = TinhTrangMo.objects.get(ma_tinh_trang="DGD")
                mo.save()

            return redirect("quan_li_giay_chung_nhan")


def thong_ke_don_hang(request, from_date=None, to_date=None):
    if from_date is None or to_date is None:
        return render(request, "thong_ke_don_hang.html")

    # Parse the dates from string to datetime objects
    from_date_obj = datetime.strptime(from_date, '%Y-%m-%d')
    to_date_obj = datetime.strptime(to_date, '%Y-%m-%d')

    # Query the 'DonHang' model instances within the date range
    dach_sach_don_hang = DonHang.objects.filter(
        Q(ngay_giao_dich__gte=from_date_obj) & Q(ngay_giao_dich__lte=to_date_obj)
    )

    all_mo = Mo.objects.all()

    total_mo = len(all_mo)
    used_mo = len(Mo.objects.filter(tinh_trang_mo=TinhTrangMo.objects.get(ma_tinh_trang="DSD")))

    # perform some simple stats
    total_value = 0
    dich_vu_count = defaultdict(int)
    for donhang in dach_sach_don_hang:
        total_value += int(donhang.gia_tri_don_hang)
        for dich_vu in donhang.danh_sach_dich_vu.all():
            dich_vu_count[dich_vu] += 1

    context = {
        "dich_vu_count": dict(dich_vu_count),
        "total_value": total_value,
        "from_date": from_date_obj.strftime("%d-%m-%Y"),
        "to_date": to_date_obj.strftime("%d-%m-%Y"),
        "total_mo": total_mo,
        "used_mo": used_mo
    }

    return render(request, "thong_ke_don_hang.html", context)
