from django.urls import path
from . import views


# url configuration
urlpatterns = [
    path('', views.welcome),
    path('login/', views.login),
    path('d_management/', views.d_management),
    path('p_dashboard/', views.p_dashboard),
    path('d_appointment/', views.d_appointment),
    path('d_dashboard/', views.d_dashboard),
    path('p_management/', views.p_management),
    path('p_prescription/', views.p_prescription),
    path('p_records/', views.p_records),
    path('p_booking/', views.p_booking),



]
