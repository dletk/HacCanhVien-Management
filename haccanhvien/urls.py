from django.urls import path

from . import views
from .admin import dich_vu_adminsite, san_pham_adminsite

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/dichvu/", dich_vu_adminsite.urls),
    path("admin/sanpham/", san_pham_adminsite.urls),
    path("so-do-du-an/", views.project_plan, name="so-do-du-an"),
]
