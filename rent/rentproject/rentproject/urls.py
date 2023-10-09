from django.contrib import admin
from django.urls import path

from.import views

urlpatterns =[
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('about_us/', views.about_us, name='about_us'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('furniture/', views.furniture, name='furniture'),
    path('appliances/', views.appliances, name='appliances'),
    path('gatgets/', views.gatgets, name='gatgets'),
    path('decoration/', views.decoration, name='decoration'),


    path('signup/', views.Handlesignup, name='signup'),

    path('signin/', views.Handlesignin, name='signin'),

]



