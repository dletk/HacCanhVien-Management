from django.db import models


class ThanhPhanDichVu(models.Model):
    ten_thanh_phan = models.CharField(verbose_name="Tên thành phần", name="ten_thanh_phan", unique=True, max_length=256)
    mieu_ta = models.TextField(verbose_name="Miêu tả", name="mieu_ta", blank=True, null=True)


class DichVu(models.Model):
    ten_dich_vu = models.CharField(verbose_name="Tên dịch vụ", name="ten_dich_vu", unique=True, max_length=256)
    ma_dich_vu = models.CharField(verbose_name="Mã dịch vụ", name="ma_dich_vu", unique=True, max_length=256)
    danh_sach_thanh_phan = models.ManyToManyField(
        ThanhPhanDichVu, to_field="ten_thanh_phan", verbose_name="Danh sách thành phần", null=True, blank=True)
    mieu_ta = models.TextField(verbose_name="Miêu tả", name="mieu_ta", blank=True, null=True)

    class Meta:
        verbose_name = "Dịch vụ"
        verbose_name_plural = "Dịch vụ"


class LoaiDichVu(models.Model):
    ten_loai_dich_vu = models.CharField("Loại dịch vụ", name="loai_dich_vu", unique=True, max_length=256)
    ma_loai_dich_vu = models.CharField("Mã loại dịch vụ", name="ma_loai_dich_vu", unique=True, max_length=256)
    danh_sach_dich_vu = models.ManyToManyField(DichVu, to_field="ten_dich_vu", verbose_name="Danh sách dịch vụ")
    mieu_ta = models.TextField(verbose_name="Miêu tả", name="mieu_ta", blank=True, null=True)
