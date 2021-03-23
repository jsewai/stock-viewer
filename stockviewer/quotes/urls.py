from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us', views.about, name="about"),
    path('add_stocks', views.add_stock, name="add_stock"),
    path('delete/<stock_id>', views.delete, name="delete")
]
