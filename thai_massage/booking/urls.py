from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('treatments/', views.treatments, name='treatments'),
    path('book-now/', views.book_now, name='book_now'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]