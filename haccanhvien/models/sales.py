from django.db import models

from .dich_vu import DichVu
from .khach_hang import KhachMua
from .san_pham import Mo, TinhTrangMo


class DonHang(models.Model):

    DANG_CHO = "DANG_CHO"
    HOAN_TAT = "HOAN_TAT"
    TRANG_THAI = [
        (DANG_CHO, "Đang chờ thanh toán"),
        (HOAN_TAT, "Hoàn tất")
    ]

    ma_don_hang = models.AutoField(verbose_name="Mã đơn hàng", primary_key=True)
    khach_mua = models.ForeignKey(KhachMua, verbose_name="Khách mua hàng", on_delete=models.RESTRICT, blank=False)
    mo = models.ForeignKey(Mo, verbose_name="Mộ", on_delete=models.RESTRICT, blank=False)
    ngay_giao_dich = models.DateField(verbose_name="Ngày giao dịch", blank=False)
    danh_sach_dich_vu = models.ManyToManyField(DichVu, verbose_name="Danh sách dịch vụ", blank=False)
    gia_tri_don_hang = models.BigIntegerField(verbose_name="Giá trị đơn hàng", blank=False)
    trang_thai = models.CharField(verbose_name="Trạng thái", max_length=256, choices=TRANG_THAI, blank=False)

    class Meta:
        verbose_name = "Đơn hàng"
        verbose_name_plural = "Đơn hàng"

    def save(self, *args, **kwargs) -> None:
        """Override the save method to create a new Giay Chung Nhan when Dong Hang is Hoan tat
        """
        # Call the original save method
        super().save(*args, **kwargs)

        # Marked the Mo associated with the new don hang as Dang Giao Dich if it is Con Trong
        if self.trang_thai == self.DANG_CHO:
            tinh_trang = self.mo.tinh_trang_mo
            if tinh_trang == TinhTrangMo.objects.get(ma_tinh_trang="CT"):
                self.mo.tinh_trang_mo = TinhTrangMo.objects.get(ma_tinh_trang="DGD")
                self.mo.save()

        # Create a new instance of Giay Chung Nhan for this Don Hang, NOTE: This is for demo purpose, this logic
        # should come from the UI for easy changes later
        if self.trang_thai == self.HOAN_TAT:
            GiayChungNhan.objects.get_or_create(don_hang=self)

    def __str__(self) -> str:
        return f"Đơn hàng cho Mộ: {self.mo.ma_mo}"


class GiayChungNhan(models.Model):

    DANG_CHO = "DANG_CHO"
    HOAN_TAT = "HOAN_TAT"
    TRANG_THAI = [
        (DANG_CHO, "Đang chờ duyệt"),
        (HOAN_TAT, "Hoàn tất")
    ]

    don_hang = models.OneToOneField(DonHang, on_delete=models.RESTRICT, blank=False)
    trang_thai = models.CharField(verbose_name="Trạng thái", max_length=256,
                                  choices=TRANG_THAI, blank=False, default=DANG_CHO)

    class Meta:
        verbose_name = "Giấy chứng nhận"
        verbose_name_plural = "Giấy chứng nhận"

    def save(self, *args, **kwargs) -> None:
        """Override the save method to marked the associated Mo as Da Ban when Giay Chung Nhan is Hoan Tat
        """
        # Call the original save method
        super().save(*args, **kwargs)

        if self.trang_thai == self.HOAN_TAT:
            mo = self.don_hang.mo
            tinh_trang_da_ban = TinhTrangMo.objects.get(ma_tinh_trang="DB")
            if mo.tinh_trang_mo != tinh_trang_da_ban:
                mo.tinh_trang_mo = tinh_trang_da_ban
                mo.save()

    def __str__(self) -> str:
        return f"Giấy chứng nhận cho Mộ: {self.don_hang.mo.ma_mo}"
