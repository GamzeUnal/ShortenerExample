from app import views 
from django.urls import path

urlpatterns = [ 
    path('api/shortener', views.post_shortener),
    path('api/shortener/<int:pk>', views.shortener_detail),
    path('<str:url>', views.redirect, name='redirect'),]