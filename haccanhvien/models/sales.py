from django.db import models

from .dich_vu import DichVu
from .khach_hang import KhachMua
from .san_pham import Mo


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


class GiayChungNhan(models.Model):

    DANG_CHO = "DANG_CHO"
    HOAN_TAT = "HOAN_TAT"
    TRANG_THAI = [
        (DANG_CHO, "Đang chờ duyệt"),
        (HOAN_TAT, "Hoàn tất")
    ]

    ma_don_hang = models.ForeignKey(DonHang, on_delete=models.RESTRICT, blank=False)
    trang_thai = models.CharField(verbose_name="Trạng thái", max_length=256,
                                  choices=TRANG_THAI, blank=False, default=DANG_CHO)

    class Meta:
        verbose_name = "Giấy chứng nhận"
        verbose_name_plural = "Giấy chứng nhận"
