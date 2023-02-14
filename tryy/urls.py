from django.contrib import admin
from django.urls import path
from tryy import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name='home'),
    path('products/',views.products,name='products/'),
    path('signup',views.signu,name='signu'),
    path('login',views.loginn,name='login'),
    path('logout',views.logoutt,name='logout'),
    path('payment',views.paymentt,name='payment')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




# 4242 4242 4242 4242

