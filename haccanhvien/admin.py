from django.contrib import admin

from .models import CapDoSanPham, KhuVuc, LoaiHang, LoaiSanPham, Mo

# Register your models here.
admin.site.register([KhuVuc, LoaiHang, LoaiSanPham, CapDoSanPham, Mo])


admin.site.site_header = "Hạc Cảnh Viên"
admin.site.site_title = "Hệ thống quản lí Hạc Cảnh Viên"
admin.site.index_title = "Chào mừng bạn đến với hệ thống quản lí - Hạc Cảnh Viên"
