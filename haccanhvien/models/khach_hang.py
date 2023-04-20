from django.db import models

from .san_pham import Mo


class KhachMua(models.Model):
    ma_khach_hang = models.AutoField(verbose_name="Mã khách hàng", primary_key=True)
    ten_khach = models.CharField(verbose_name="Têm khách hàng", name="ten_khach_mua", blank=False, max_length=256)
    CCCD = models.CharField(verbose_name="Số CMND/CCCD", name="CCCD", blank=False, max_length=20)
    so_dien_thoai = models.CharField(verbose_name="Số điện thoại", name="so_dien_thoai", max_length=20)
    dia_chi = models.TextField(verbose_name="Địa chỉ", name="dia_chi")

    class Meta:
        verbose_name = "Khách mua hàng"
        verbose_name_plural = "Khách mua hàng"


class KhachMat(models.Model):
    ma_khach_hang = models.AutoField(verbose_name="Mã khách hàng", primary_key=True)
    ten_khach = models.CharField(verbose_name="Tên khách", name="ten_khach", blank=False, max_length=256)
    ngay_mat = models.DateField(verbose_name="Ngày mất", name="ngay_mat", blank=False)
    mo = models.ForeignKey(Mo, verbose_name="Mộ chôn", blank=False, on_delete=models.CASCADE)
    thong_tin_khac = models.TextField(verbose_name="Thông tin khác")

    class Meta:
        verbose_name = "Khách sử dụng mộ"
        verbose_name_plural = "Khách sử dụng mộ"


class KyUc(models.Model):
    ma_khach_hang = models.OneToOneField(KhachMat, on_delete=models.CASCADE, verbose_name="Mã khách hàng")

    class Meta:
        verbose_name = "Ký ức"
        verbose_name_plural = "Ký ức"


class AnhKyUc(models.Model):
    ma_ky_uc = models.ForeignKey(KyUc, on_delete=models.CASCADE, verbose_name="Ký ức")
    image = models.ImageField("Ảnh", name="image")

    class Meta:
        verbose_name = "Ảnh ký ức"
        verbose_name_plural = "Ảnh ký ức"
