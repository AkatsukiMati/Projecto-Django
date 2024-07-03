from django.urls import path
from . import views

urlpatterns = [
    path('Main', views.Main , name="Main" ),
    path('hyundai', views.hyundai , name="hyundai" ),
    path('compra', views.compra , name="compra" ),
    path('chevrolet', views.chevrolet , name="chevrolet" ),
    path('About', views.About , name="About" ),
    
]
