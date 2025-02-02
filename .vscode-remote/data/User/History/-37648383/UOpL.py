from django.db import models
from django.contrib.auth.models import User


class Treatments(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    half_hour = models.DecimalField(max_digits=6, decimal_places=2, default=55.00)
    one_hour = models.DecimalField(max_digits=6, decimal_places=2, default=80.00)
    two_hour = models.DecimalField(max_digits=6, decimal_places=2, default=110.00)
    

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
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Auto-calculate end time based on duration
        from datetime import datetime, timedelta
        start = datetime.combine(self.date, self.start_time)
        duration = self.get_duration_minutes()
        self.end_time = (start + timedelta(minutes=duration)).time()
        super().save(*args, **kwargs)

    def get_duration_minutes(self):
        # Map duration to minutes based on treatment pricing
        if self.treatment.half_hour:
            return 30
        elif self.treatment.one_hour:
            return 60
        elif self.treatment.two_hour:
            return 120
        return 0

    def __str__(self):
        duration = get_duration_minutes()
        return f"{self.user.username} - {self.treatment.title} on {self.date} at {self.start_time} for {self.duration} mins"