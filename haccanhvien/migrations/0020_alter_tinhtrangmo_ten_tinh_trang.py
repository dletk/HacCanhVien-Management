# Generated by Django 4.1.7 on 2023-04-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haccanhvien', '0019_remove_tinhtrangmo_loai_tinh_trang_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tinhtrangmo',
            name='ten_tinh_trang',
            field=models.CharField(max_length=256, unique=True, verbose_name='Tên tình trạng'),
        ),
    ]
