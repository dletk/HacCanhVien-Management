# Generated by Django 4.1.7 on 2023-03-28 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('haccanhvien', '0005_remove_loaidichvu_danh_sach_dich_vu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dichvu',
            name='loai_dich_vu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haccanhvien.loaidichvu', to_field='ma_loai_dich_vu', verbose_name='Loại dịch vụ'),
        ),
    ]
