from django.db import models

# Create your models here.


class KhuVuc(models.Model):
    ma_khu_vuc = models.CharField("Mã khu vực", name="ma_khu_vuc", max_length=256, unique=True)
    ten_hien_thi = models.CharField("Tên hiển thị", name="ten_hien_thi", max_length=256)
    mieu_ta = models.TextField("Miêu tả", name="mieu_ta")
    description = models.CharField(max_length=255, null=True, blank=True,
                                   help_text="Khu vực được hiểu là một khu trong bản đồ quy hoạch tổng thể, có thể chứa các loại sản phảm tương tự nhau.")

    class Meta:
        verbose_name = "Khu vực"
        verbose_name_plural = "Khu vực"

    def __str__(self) -> str:
        return self.ten_hien_thi


class CapDoSanPham(models.Model):
    ma_cap_do = models.CharField("Mã cấp độ", name="ma_cap_do", unique=True, max_length=256)
    ten_cap_do = models.CharField("Tên cấp độ", name="ten_cap_do", max_length=256, null=True, blank=True)
    mieu_ta = models.TextField("Miêu tả", name="mieu ta")

    def save(self, *args, **kwargs) -> None:
        """Override the save method to update the foreign key value when it is changed
        """
        # Get the old object before saving the changes
        try:
            old_obj = CapDoSanPham.objects.get(pk=self.pk)
        except CapDoSanPham.DoesNotExist:
            old_obj = None

        # Call the original save method
        super().save(*args, **kwargs)

        # Update the foreign key in the related model
        if old_obj and old_obj.ma_cap_do != self.ma_cap_do:
            LoaiHang.objects.filter(ma_cap_do=old_obj.ma_cap_do).update(ma_cap_do=self.ma_cap_do)

    def __str__(self) -> str:
        return self.ma_cap_do

    class Meta:
        verbose_name = "Cấp độ sản phẩm"
        verbose_name_plural = "Cấp độ sản phẩm"


class LoaiSanPham(models.Model):
    ma_san_pham = models.CharField("Mã sản phẩm", name="ma_san_pham", unique=True, max_length=256)
    ten_san_pham = models.CharField("Tên sản phẩm", name="ten_san_pham", max_length=256)
    mieu_ta = models.TextField("Miêu tả", name="mieu_ta")

    def save(self, *args, **kwargs) -> None:
        """Override the save method to update the foreign key value when it is changed
        """
        # Get the old object before saving the changes
        try:
            old_obj = LoaiSanPham.objects.get(pk=self.pk)
        except LoaiSanPham.DoesNotExist:
            old_obj = None

        # Call the original save method
        super().save(*args, **kwargs)

        # Update the foreign key in the related model
        if old_obj and old_obj.ma_san_pham != self.ma_san_pham:
            LoaiHang.objects.filter(ma_san_pham=old_obj.ma_san_pham).update(ma_san_pham=self.ma_san_pham)

    def __str__(self) -> str:
        return f"{self.ten_san_pham} | Mã: {self.ma_san_pham}"

    class Meta:
        verbose_name = "Mã sản phẩm"
        verbose_name_plural = "Mã sản phẩm"


class LoaiHang(models.Model):
    ma_hang = models.CharField("Mã hàng", name="ma_hang", unique=True, max_length=256)
    ten_ma_hang = models.CharField("Tên mã hàng", name="ten_ma_hang", blank=True, null=True, max_length=256)
    ma_san_pham = models.ForeignKey(LoaiSanPham, on_delete=models.CASCADE,
                                    verbose_name="Mã sản phẩm", to_field="ma_san_pham")
    ma_cap_do = models.ForeignKey(CapDoSanPham, on_delete=models.CASCADE,
                                  verbose_name="Mã cấp độ", to_field="ma_cap_do")

    class Meta:
        verbose_name = "Loại hàng"
        verbose_name_plural = "Loại hàng"

    def __str__(self) -> str:
        return f"{self.ten_ma_hang}"


class TinhTrangMo(models.Model):
    ten_tinh_trang = models.CharField(verbose_name="Tên tình trạng",
                                      name="ten_tinh_trang", max_length=256, unique=True)
    ma_tinh_trang = models.CharField(verbose_name="Mã tình trạng", name="ma_tinh_trang", max_length=256, unique=True)

    class Meta:
        verbose_name = "Tình trạng mộ"
        verbose_name_plural = "Tình trạng mộ"

    def __str__(self) -> str:
        return self.ten_tinh_trang

    def save(self, *args, **kwargs) -> None:
        """Override the save method to update the foreign key value when it is changed
        """
        # Get the old object before saving the changes
        try:
            old_obj = TinhTrangMo.objects.get(pk=self.pk)
        except TinhTrangMo.DoesNotExist:
            old_obj = None

        # Call the original save method
        super().save(*args, **kwargs)

        # Update the foreign key in the related model
        if old_obj and old_obj.ma_tinh_trang != self.ma_tinh_trang:
            Mo.objects.filter(tinh_trang_mo=old_obj.ma_tinh_trang).update(tinh_trang_mo=self.ma_tinh_trang)


class Mo(models.Model):
    ma_khu_vuc = models.ForeignKey(KhuVuc, on_delete=models.RESTRICT, verbose_name="Mã khu vực", to_field="ma_khu_vuc")
    ma_hang = models.ForeignKey(LoaiHang, on_delete=models.RESTRICT, verbose_name="Loại hàng", to_field="ma_hang")
    hang = models.IntegerField(verbose_name="Vị trí hàng", name="hang")
    cot = models.IntegerField(verbose_name="Vị trí cột", name="cot")
    ma_mo = models.CharField("Mã mộ", name="ma_mo", max_length=256, blank=True, null=True)
    tinh_trang_mo = models.ForeignKey(TinhTrangMo, on_delete=models.RESTRICT,
                                      verbose_name="Tình trạng mộ", to_field="ma_tinh_trang")

    class Meta:
        unique_together = ["hang", "cot", "ma_khu_vuc"]
        verbose_name = "Phần mộ"
        verbose_name_plural = "Phần mộ"

    def __str__(self) -> str:
        return f"{self.ma_hang} | Khu: {self.ma_khu_vuc} | Hàng: {self.hang} | Cột: {self.cot}"
