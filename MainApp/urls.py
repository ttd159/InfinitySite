from django.urls import path
from . import views

urlpatterns = [
    path('', views.angiang, name='index'),
    path('angiang/', views.angiang, name='angiang'),
    path('tiengiang/', views.tiengiang, name='tiengiang'),
    path('soctrang/', views.soctrang, name='soctrang'),
]
