import os
from django.conf import settings
from django.shortcuts import render
import qrcode
from QRCODE.forms import QRCodeForm
# Create your views here.


def index(request):
    return render(request,'qrcode/index.html')


def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']
            
            
            # generation QRCODE
            qr = qrcode.make(url)
            file_name = res_name.replace(" ","_").lower()+'_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)
            
            # creation image url
            qr_url = os.path.join(settings.MEDIA_URL, file_name)
            
            context = {
                'res_name':res_name,
                'qr_url':qr_url,
                
                }
            return render(request, 'qrcode/qr_result.html', context)
            
            
    else:
        form = QRCodeForm()
    context = {
        'form':form,
    }
    return render(request,'qrcode/generate_qr_code.html', context)