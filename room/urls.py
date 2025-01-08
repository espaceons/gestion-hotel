from django.urls import path
from room import views

app_name='Room'

urlpatterns = [
    path('',views.index, name="index"),
    path('update/<int:pk>',views.update, name="update"),
]
