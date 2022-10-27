from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('login/', views.login, name='login'),
    path('usuario/', views.usuario, name='usuario'),
    path('inicioU/', views.inicioU, name='inicioU'),
    path('contactoU/', views.contactoU, name='contactoU'),
    path('catalogoU/', views.catalogoU, name='catalogoU'),
    path('nosotrosU/', views.nosotrosU, name='nosotrosU'),
    
]