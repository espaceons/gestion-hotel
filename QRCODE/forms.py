from django import forms


class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(max_length=50,
                                      widget=forms.TextInput(attrs={
                                          'class':'form-control',
                                          'placeholder':'entre nom restaurant',
                                          
                                      }))
    url = forms.URLField(max_length=200,
                         label='Menu URL Retaurant',
                         widget= forms.URLInput(attrs={
                             'class':'form-control',
                             'placeholder':'url menu en ligne'
                         })
                         )