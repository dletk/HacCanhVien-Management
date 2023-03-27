from django.contrib import admin

from .models.san_pham import CapDoSanPham, KhuVuc, LoaiHang, LoaiSanPham, Mo

# Register your models here.
admin.site.register([KhuVuc, LoaiSanPham, CapDoSanPham, Mo])

class LoaiHangAdmin(admin.ModelAdmin):
    list_filter = ["ma_san_pham", "ma_cap_do"]

admin.site.register(LoaiHang, LoaiHangAdmin)

admin.site.site_header = "Hạc Cảnh Viên"
admin.site.site_title = "Hệ thống quản lí Hạc Cảnh Viên"
admin.site.index_title = "Chào mừng bạn đến với hệ thống quản lí - Hạc Cảnh Viên"
