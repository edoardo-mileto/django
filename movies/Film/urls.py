from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:film_id>/', views.detail, name='detail'),
    path('Attori/<int:attore_id>/', views.attore, name='attore'),
    path('Registi/<int:regista_id>/', views.regista, name='regista')
]