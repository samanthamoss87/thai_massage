from django.db import models

class Treatments(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    half_hour = models.DecimalField(max_digits=6, decimal_places=2, default=55.00)
    one_hour = models.DecimalField(max_digits=6, decimal_places=2, default=55.00)
    two_hour = models.DecimalField(max_digits=6, decimal_places=2, default=55.00)
    

    def __str__(self):
        return f"{self.title}"