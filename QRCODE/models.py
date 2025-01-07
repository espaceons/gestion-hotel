from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import qrcode




# Create your models here.

class QR_code(models.Model):
    data = models.CharField(max_length=255)
    qr_code = models.ImageField(upload_to='qr_code', null=True, blank=True)
    
    
    def __str__(self):
        return  self.data
        