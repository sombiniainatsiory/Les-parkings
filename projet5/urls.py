
from django.contrib import admin
from django.urls import path

from auth_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.acceuil, name='acceuil'),
    path('inscription/',views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('home/', views.home, name='home'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
]
