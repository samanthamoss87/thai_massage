from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('treatments/', views.treatments, name='treatments'),
    path('book-now/', views.book_now, name='book_now'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('cancel-booking/<int:booking_id>/', cancel_booking, name='cancel_booking'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]