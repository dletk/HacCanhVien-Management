from django.urls import path

from . import views
from .admin import dich_vu_adminsite, san_pham_adminsite

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/dichvu/", dich_vu_adminsite.urls),
    path("admin/sanpham/", san_pham_adminsite.urls),
    path("so-do-du-an/", views.ban_hang, name="so-do-du-an"),
    path("order/", views.order, name="order"),
    path("order/<int:customer_id>/", views.order, name="existing_customer_order"),
    path("quan-li-don-hang/", views.quan_li_don_hang_dang, name="quan_li_don_hang"),
    path("quan-li-don-hang/<int:ma_don_hang>/<slug:trang_thai>",
         views.quan_li_don_hang_dang, name="doi_trang_thai_don_hang"),
]
