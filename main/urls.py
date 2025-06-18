from django.urls import path
from . import views
from django.shortcuts import render

def test_form(request):
    return render(request, 'main/test_form.html')

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('test-form/', test_form, name='test_form'),
    path('api/horoscope/<str:sign>/', views.horoscope_api, name='horoscope_api'),
]
