from django.db import models

# Create your models here.


class KhuVuc(models.Model):
    ma_khu_vuc = models.CharField("Mã khu vực", name="ma_khu_vuc", primary_key=True, max_length=256)
    ten_hien_thi = models.CharField("Tên hiển thị", name="ten_hien_thi", max_length=256)
    mieu_ta = models.TextField("Miêu tả", name="mieu_ta")

    class Meta:
        verbose_name = "Khu vực"
        verbose_name_plural = "Khu vực"

    def __str__(self) -> str:
        return self.ten_hien_thi


class CapDoSanPham(models.Model):
    ma_cap_do = models.CharField("Mã cấp độ", name="ma_cap_do", primary_key=True, max_length=256)
    mieu_ta = models.TextField("Miêu tả", name="mieu ta")

    def __str__(self) -> str:
        return self.ma_cap_do

    class Meta:
        verbose_name = "Cấp độ sản phẩm"
        verbose_name_plural = "Cấp độ sản phẩm"


class LoaiSanPham(models.Model):
    ma_san_pham = models.CharField("Mã sản phẩm", name="ma_san_pham", primary_key=True, max_length=256)
    mieu_ta = models.TextField("Miêu tả", name="mieu_ta")

    def __str__(self) -> str:
        return self.ma_san_pham

    class Meta:
        verbose_name = "Mã sản phẩm"
        verbose_name_plural = "Mã sản phẩm"


class LoaiHang(models.Model):
    ma_hang = models.CharField("Mã hàng", name="ma_hang", primary_key=True, max_length=256)
    ma_san_pham = models.ForeignKey(LoaiSanPham, on_delete=models.CASCADE, verbose_name="Mã sản phẩm")
    ma_cap_do = models.ForeignKey(CapDoSanPham, on_delete=models.CASCADE, verbose_name="Mã cấp độ")

    class Meta:
        verbose_name = "Loại hàng"
        verbose_name_plural = "Loại hàng"

    def __str__(self) -> str:
        return f"{self.ma_hang} | {self.ma_san_pham} | {self.ma_cap_do}"


class Mo(models.Model):
    ma_mo = models.CharField("Mã mộ", name="ma_mo", primary_key=True, max_length=256)
    ma_khu_vuc = models.ForeignKey(KhuVuc, on_delete=models.RESTRICT, verbose_name="Mã khu vực")
    ma_hang = models.ForeignKey(LoaiHang, on_delete=models.RESTRICT, verbose_name="Loại hàng")
    hang = models.IntegerField(verbose_name="Vị trí hàng", name="hang")
    cot = models.IntegerField(verbose_name="Vị trí cột", name="cot")

    class Meta:
        unique_together = ["hang", "cot", "ma_khu_vuc"]
        verbose_name = "Phần mộ"
        verbose_name_plural = "Phần mộ"

    def __str__(self) -> str:
        return f"{self.ma_mo} | Khu: {self.ma_khu_vuc} | Hàng: {self.hang} | Cột: {self.cot}"
