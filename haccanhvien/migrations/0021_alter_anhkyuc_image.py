# Generated by Django 4.1.7 on 2023-04-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haccanhvien', '0020_alter_tinhtrangmo_ten_tinh_trang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anhkyuc',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Ảnh'),
        ),
    ]
