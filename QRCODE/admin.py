from django.contrib import admin
from QRCODE.models import QR_code
# Register your models here.

@admin.register(QR_code)
class QR_codeModelAdmin(admin.ModelAdmin):
    list_display = ('data','qr_code')