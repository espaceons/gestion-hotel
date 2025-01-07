
from django.urls import path

from QRCODE import views

name_app = 'QRCODE'

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.generate_qr_code, name="generate_qr_code"),
]
