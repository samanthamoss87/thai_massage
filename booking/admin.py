from django.contrib import admin
from .models import Treatments, Booking, UserProfile, Contact

admin.site.register(Treatments)
admin.site.register(Booking)
admin.site.register(UserProfile)
admin.site.register(Contact)
