from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('services/', views.services_page, name='services'),
    path('book/<int:service_id>/', views.book_service, name='book_service'),
]
