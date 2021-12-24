from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('book/<slug:slug>/', views.product_detail, name='product_detail'),
    path('books/<slug:slug>/', views.category_list, name='category_list'),
]