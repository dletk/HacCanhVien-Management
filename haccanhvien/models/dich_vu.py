from django.db import models


class DichVu(models.Model):
    ten_dich_vu = models.CharField(verbose_name="Tên dịch vụ", name="ten_dich_vu", primary_key=True, max_length=256)
    mieu_ta = models.TextField(verbose_name="Miêu tả", name="mieu_ta", blank=True, null=True)
