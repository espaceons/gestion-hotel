# Generated by Django 5.1.4 on 2025-01-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QRCODE', '0002_alter_qr_code_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr_code',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_code'),
        ),
    ]