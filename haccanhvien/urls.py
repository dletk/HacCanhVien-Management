from django.urls import path

from . import views
from .admin import dich_vu_adminsite, san_pham_adminsite

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/dichvu/", dich_vu_adminsite.urls),
    path("admin/sanpham/", san_pham_adminsite.urls),
    path("so-do-du-an/", views.ban_hang, name="so-do-du-an"),
    path("order/", views.dat_hang, name="order"),
    path("order/<int:customer_id>/", views.dat_hang, name="existing_customer_order"),
    path("quan-li-don-hang/", views.quan_li_don_hang, name="quan_li_don_hang"),
    path("quan-li-don-hang/<int:ma_don_hang>/<slug:trang_thai>",
         views.quan_li_don_hang, name="doi_trang_thai_don_hang"),
    path("thong-tin-nguoi-mat/<int:moid>", views.thong_tin_nguoi_mat, name="thong_tin_nguoi_mat"),
    path("thong-tin-nguoi-mat/add/<int:moid>", views.add_nguoi_mat, name="add_nguoi_mat"),
    path("quan-li-giay-chung-nhan/", views.quan_li_giay_chung_nhan, name="quan_li_giay_chung_nhan"),
    path("quan-li-giay-chung-nhan/<int:giay_chung_nhan_id>/<slug:trang_thai>",
         views.quan_li_giay_chung_nhan, name="doi_trang_thai_giay_chung_nhan"),
]
