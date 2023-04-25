from django.urls import path

from . import views
from .admin import dich_vu_adminsite, san_pham_adminsite

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/dichvu/", dich_vu_adminsite.urls),
    path("admin/sanpham/", san_pham_adminsite.urls),
    path("so-do-du-an/", views.ban_hang, name="so-do-du-an"),
    path("order/", views.order, name="existing_customer_order"),
    path("order/<int:customer_id>/", views.order, name="new_customer_order"),
]
