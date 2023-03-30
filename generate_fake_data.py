
from haccanhvien.models.san_pham import KhuVuc, LoaiHang, Mo

# create the LoaiHang object with ma_hang = "DNM-TA-VIP*"
loaihang = LoaiHang.objects.get(ma_hang="HD-TC")

# get the KhuVuc object with ma_khu_vuc starting with "F"
khuvuc = KhuVuc.objects.get(ma_khu_vuc__startswith='F')

# generate fake Mo objects for the KhuVuc object
for hang in range(3, 6):
    for cot in range(1, 41):
        # generate a random string for ma_mo
        ma_mo = f"{khuvuc.ma_khu_vuc}-{hang}-{cot}"

        # create the Mo object with the generated values
        mo = Mo(
            ma_khu_vuc=khuvuc,
            ma_hang=loaihang,
            hang=hang,
            cot=cot,
            ma_mo=ma_mo
        )

        # save the Mo object to the database
        mo.save()
