from django.db import models


class LoaiDichVu(models.Model):
    ten_loai_dich_vu = models.CharField("Loại dịch vụ", name="ten_loai_dich_vu", unique=True, max_length=256)
    ma_loai_dich_vu = models.CharField("Mã loại dịch vụ", name="ma_loai_dich_vu", unique=True, max_length=256)
    mieu_ta = models.TextField(verbose_name="Miêu tả", name="mieu_ta", blank=True, null=True)

    class Meta:
        verbose_name = "Loại Dịch vụ"
        verbose_name_plural = "Loại Dịch vụ"

    def __str__(self) -> str:
        return self.ten_loai_dich_vu

    def save(self, *args, **kwargs) -> None:
        """Override the save method to update the foreign key value when it is changed
        """
        # Get the old object before saving the changes
        try:
            old_obj = LoaiDichVu.objects.get(pk=self.pk)
        except LoaiDichVu.DoesNotExist:
            old_obj = None

        # Call the original save method
        super().save(*args, **kwargs)

        # Update the foreign key in the related model
        if old_obj and old_obj.ma_loai_dich_vu != self.ma_loai_dich_vu:
            DichVu.objects.filter(ma_loai_dich_vu=old_obj.ma_loai_dich_vu).update(
                ma_loai_dich_vu=self.ma_loai_dich_vu)
            LoaiDichVu.objects.filter(ma_loai_dich_vu=old_obj.ma_loai_dich_vu).update(
                ma_loai_dich_vu=self.ma_loai_dich_vu
            )


class ThanhPhanDichVu(models.Model):
    ten_thanh_phan = models.CharField(verbose_name="Tên thành phần", name="ten_thanh_phan", unique=True, max_length=256)
    ma_thanh_phan = models.CharField(verbose_name="Mã thành phần", name="ma_thanh_phan", unique=True, max_length=256)
    ma_loai_dich_vu = models.ForeignKey(LoaiDichVu, on_delete=models.CASCADE,
                                        verbose_name="Mã loại dịch vụ", to_field="ma_loai_dich_vu")
    mieu_ta = models.TextField(verbose_name="Miêu tả", name="mieu_ta", blank=True, null=True)

    class Meta:
        verbose_name = "Thành phần Dịch vụ"
        verbose_name_plural = "Thành phần Dịch vụ"

    def __str__(self) -> str:
        return self.ten_thanh_phan


class DichVu(models.Model):
    ten_dich_vu = models.CharField(verbose_name="Tên dịch vụ", name="ten_dich_vu", unique=True, max_length=256)
    ma_dich_vu = models.CharField(verbose_name="Mã dịch vụ", name="ma_dich_vu", unique=True, max_length=256)
    loai_dich_vu = models.ForeignKey(LoaiDichVu, on_delete=models.CASCADE,
                                     to_field="ma_loai_dich_vu", verbose_name="Loại dịch vụ")
    danh_sach_thanh_phan = models.ManyToManyField(
        ThanhPhanDichVu, verbose_name="Danh sách thành phần", null=True, blank=True)
    mieu_ta = models.TextField(verbose_name="Miêu tả", name="mieu_ta", blank=True, null=True)

    class Meta:
        verbose_name = "Dịch vụ"
        verbose_name_plural = "Dịch vụ"

    def __str__(self) -> str:
        return self.ten_dich_vu
