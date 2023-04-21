from django.db import models

from .san_pham import Mo


class KhachMua(models.Model):
    ma_khach_hang = models.AutoField(verbose_name="Mã khách hàng", primary_key=True)
    ten_khach = models.CharField(verbose_name="Têm khách hàng", blank=False, max_length=256)
    CCCD = models.CharField(verbose_name="Số CMND/CCCD", blank=False, max_length=20)
    so_dien_thoai = models.CharField(verbose_name="Số điện thoại", max_length=20)
    dia_chi = models.TextField(verbose_name="Địa chỉ")

    class Meta:
        verbose_name = "Khách mua hàng"
        verbose_name_plural = "Khách mua hàng"

    def __str__(self) -> str:
        return f"{self.ten_khach} - SDT: {self.so_dien_thoai}"


class KhachMat(models.Model):
    ma_khach_hang = models.AutoField(verbose_name="Mã khách hàng", primary_key=True)
    ten_khach = models.CharField(verbose_name="Tên khách", blank=False, max_length=256)
    ngay_mat = models.DateField(verbose_name="Ngày mất", blank=False)
    mo = models.ForeignKey(Mo, verbose_name="Mộ chôn", blank=False, on_delete=models.CASCADE)
    thong_tin_khac = models.TextField(verbose_name="Thông tin khác", blank=True)

    class Meta:
        verbose_name = "Khách sử dụng mộ"
        verbose_name_plural = "Khách sử dụng mộ"

    def __str__(self) -> str:
        return f"{self.ten_khach} - Ngày mất: {self.ngay_mat}"


class KyUc(models.Model):
    khach_hang = models.OneToOneField(KhachMat, on_delete=models.CASCADE, verbose_name="Khách hàng")

    class Meta:
        verbose_name = "Ký ức"
        verbose_name_plural = "Ký ức"

    def __str__(self) -> str:
        return f"Ký ức Khách: {self.khach_hang}"


class AnhKyUc(models.Model):
    ma_ky_uc = models.ForeignKey(KyUc, on_delete=models.CASCADE, verbose_name="Ký ức")
    image = models.ImageField("Ảnh", name="image")

    class Meta:
        verbose_name = "Ảnh ký ức"
        verbose_name_plural = "Ảnh ký ức"
