from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),
]


handler404 = 'thai_massage.views.custom_404'
