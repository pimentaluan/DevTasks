from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('registrar/', views.registrar, name='registrar'),
    path('logout/', views.logout, name='logout'),
]