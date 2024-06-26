# Generated by Django 4.1.7 on 2023-04-20 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haccanhvien', '0012_alter_khachmat_thong_tin_khac'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anhkyuc',
            options={'verbose_name': 'Ảnh ký ức', 'verbose_name_plural': 'Ảnh ký ức'},
        ),
        migrations.AlterModelOptions(
            name='donhang',
            options={'verbose_name': 'Đơn hàng', 'verbose_name_plural': 'Đơn hàng'},
        ),
        migrations.AlterModelOptions(
            name='giaychungnhan',
            options={'verbose_name': 'Giấy chứng nhận', 'verbose_name_plural': 'Giấy chứng nhận'},
        ),
        migrations.AlterModelOptions(
            name='khachmat',
            options={'verbose_name': 'Khách sử dụng mộ', 'verbose_name_plural': 'Khách sử dụng mộ'},
        ),
        migrations.AlterModelOptions(
            name='khachmua',
            options={'verbose_name': 'Khách mua hàng', 'verbose_name_plural': 'Khách mua hàng'},
        ),
        migrations.AlterModelOptions(
            name='kyuc',
            options={'verbose_name': 'Ký ức', 'verbose_name_plural': 'Ký ức'},
        ),
    ]
