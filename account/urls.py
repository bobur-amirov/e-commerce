from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.user_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>', views.account_activate, name='activate'),
]
