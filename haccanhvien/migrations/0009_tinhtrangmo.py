# Generated by Django 4.1.7 on 2023-03-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haccanhvien', '0008_thanhphandichvu_ma_loai_dich_vu'),
    ]

    operations = [
        migrations.CreateModel(
            name='TinhTrangMo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loai_tinh_trang', models.CharField(max_length=256, unique=True, verbose_name='Loại tình trạng')),
                ('ma_tinh_trang', models.CharField(max_length=256, unique=True, verbose_name='Mã tình trạng')),
            ],
        ),
    ]
