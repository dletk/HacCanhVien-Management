# Generated by Django 4.1.7 on 2023-04-20 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('haccanhvien', '0010_alter_tinhtrangmo_options_mo_tinh_trang_mo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonHang',
            fields=[
                ('ma_don_hang', models.AutoField(primary_key=True, serialize=False, verbose_name='Mã đơn hàng')),
                ('ngay_giao_dich', models.DateField(verbose_name='Ngày giao dịch')),
                ('gia_tri_don_hang', models.BigIntegerField(verbose_name='Giá trị đơn hàng')),
                ('trang_thai', models.CharField(choices=[('DANG_CHO', 'Đang chờ thanh toán'), ('HOAN_TAT', 'Hoàn tất')], max_length=256, verbose_name='Trạng thái')),
                ('danh_sach_dich_vu', models.ManyToManyField(to='haccanhvien.dichvu', verbose_name='Danh sách dịch vụ')),
            ],
        ),
        migrations.CreateModel(
            name='KhachMat',
            fields=[
                ('ma_khach_hang', models.AutoField(primary_key=True, serialize=False, verbose_name='Mã khách hàng')),
                ('ten_khach', models.CharField(max_length=256, verbose_name='Tên khách')),
                ('ngay_mat', models.DateField(verbose_name='Ngày mất')),
                ('thong_tin_khac', models.TextField(verbose_name='Ngày mất')),
                ('mo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haccanhvien.mo', verbose_name='Mộ chôn')),
            ],
        ),
        migrations.CreateModel(
            name='KhachMua',
            fields=[
                ('ma_khach_hang', models.AutoField(primary_key=True, serialize=False, verbose_name='Mã khách hàng')),
                ('ten_khach_mua', models.CharField(max_length=256, verbose_name='Têm khách hàng')),
                ('CCCD', models.CharField(max_length=20, verbose_name='Số CMND/CCCD')),
                ('so_dien_thoai', models.CharField(max_length=20, verbose_name='Số điện thoại')),
                ('dia_chi', models.TextField(verbose_name='Địa chỉ')),
            ],
        ),
        migrations.CreateModel(
            name='KyUc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_khach_hang', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='haccanhvien.khachmat', verbose_name='Mã khách hàng')),
            ],
        ),
        migrations.CreateModel(
            name='GiayChungNhan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trang_thai', models.CharField(choices=[('DANG_CHO', 'Đang chờ duyệt'), ('HOAN_TAT', 'Hoàn tất')], default='DANG_CHO', max_length=256, verbose_name='Trạng thái')),
                ('ma_don_hang', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='haccanhvien.donhang')),
            ],
        ),
        migrations.AddField(
            model_name='donhang',
            name='khach_mua',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='haccanhvien.khachmua', verbose_name='Khách mua hàng'),
        ),
        migrations.AddField(
            model_name='donhang',
            name='mo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='haccanhvien.mo', verbose_name='Mộ'),
        ),
        migrations.CreateModel(
            name='AnhKyUc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Ảnh')),
                ('ma_ky_uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haccanhvien.kyuc', verbose_name='Ký ức')),
            ],
        ),
    ]