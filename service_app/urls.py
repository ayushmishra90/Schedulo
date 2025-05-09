from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='home'),  # root `/` now shows services
    path('services/', views.services, name='services'),
    path('add/', views.add_service, name='add_service'),
    path('<int:service_id>/book/', views.book_service, name='book_service'),
    path('register/', views.register, name='register'),
    path('bookings/', views.view_bookings, name='view_bookings'),
    path('bookings/update/<int:booking_id>/', views.update_booking_status, name='update_booking_status'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('booking/<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('my-services/', views.my_services, name='my_services'),
    path('my-services/delete/<int:service_id>/', views.delete_service, name='delete_service'),
    path('booking-success/<int:booking_id>/', views.booking_success, name='booking_success')

]
