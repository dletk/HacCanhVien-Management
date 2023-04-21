
from django.http import HttpResponse
from django.shortcuts import render

from .models.san_pham import LoaiSanPham, Mo


def get_all_mo_in_grouped_objects():
    all_mo = Mo.objects.all()

    grouped_objects = []

    for obj in all_mo:
        grouped_objects.append((obj.hang, obj.cot, obj))

    context = {'grouped_objects': grouped_objects}
    return context

# Create your views here.


def index(request):
    return HttpResponse("Hello, world! Small step towards a big system!")


def ban_hang(request):
    context = get_all_mo_in_grouped_objects()

    all_ma_san_pham = LoaiSanPham.objects.all()
    context["all_ma_san_pham"] = all_ma_san_pham

    return render(request, "ban_hang.html", context)
