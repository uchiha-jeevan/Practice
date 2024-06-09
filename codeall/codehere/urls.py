

from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('calc',views.check,name='calc'),
    path('prime',views.primecheck,name='prime'),
    path('numbercheck',views.numcheck,name='numbercheck'),
    path('inbetween',views.inbetween,name='inbetween'),
]