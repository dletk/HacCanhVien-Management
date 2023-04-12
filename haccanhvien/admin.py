from django.contrib import admin
from django.contrib.admin.sites import AdminSite

from .models.dich_vu import DichVu, LoaiDichVu, ThanhPhanDichVu
from .models.san_pham import (CapDoSanPham, KhuVuc, LoaiHang, LoaiSanPham, Mo,
                              TinhTrangMo)


class SanPhamAdminSite(AdminSite):
    site_header = 'Sản phẩm'


class DichVuAdminSite(AdminSite):
    site_header = 'Dịch vụ'


class LoaiHangAdmin(admin.ModelAdmin):
    list_filter = ["ma_san_pham", "ma_cap_do"]


dich_vu_adminsite = DichVuAdminSite(name="dichvuAdmin")
san_pham_adminsite = SanPhamAdminSite(name="sanphamAdmin")

# Register your models here.
san_pham_adminsite.register([KhuVuc, LoaiSanPham, CapDoSanPham, Mo, TinhTrangMo])
san_pham_adminsite.register(LoaiHang, LoaiHangAdmin)

dich_vu_adminsite.register([LoaiDichVu, DichVu, ThanhPhanDichVu])


admin.site.register([KhuVuc, LoaiSanPham, CapDoSanPham, Mo, TinhTrangMo])
admin.site.register(LoaiHang, LoaiHangAdmin)
admin.site.register([LoaiDichVu, DichVu, ThanhPhanDichVu])


admin.site.site_header = "Hạc Cảnh Viên"
admin.site.site_title = "Hệ thống quản lí Hạc Cảnh Viên"
admin.site.index_title = "Chào mừng bạn đến với hệ thống quản lí - Hạc Cảnh Viên"
