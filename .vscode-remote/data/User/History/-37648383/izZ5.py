from django.db import models
from django.contrib.auth.models import User


class Treatments(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    half_hour = models.DecimalField(max_digits=6, decimal_places=2, default=55.00)
    one_hour = models.DecimalField(max_digits=6, decimal_places=2, default=55.00)
    two_hour = models.DecimalField(max_digits=6, decimal_places=2, default=55.00)
    

    def __str__(self):
        return f"{self.title}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


# Treatment Booking Model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatments, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField(choices=[(30, '30 minutes'), (60, '1 hour'), (120, '2 hours')])
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.treatment.title} on {self.date} at {self.time}"