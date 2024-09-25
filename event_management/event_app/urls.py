from django.urls import path
from . import views




urlpatterns=[
    path('',views.index,name='index'),
    path('gallery/',views.gallery,name='gallery'),
    path('booking/',views.booking,name='booking'),
    path('contact/',views.contact,name='contact'),
    path('home',views.home,name='home'),

    path('testhttp/<str:name>/<int:year>/<str:branch>',views.samphttp,name='testhttp'),
] 


