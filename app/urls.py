from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/<str:name>', views.menu, name='menu'),
    path('menu/item/<str:name>', views.items, name='items'),
]
