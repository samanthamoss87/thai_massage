from django.db import models

class Treatments(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    half_hour = models.DecimalField(max_digits=2)
    one_hour = models.DecimalField()
    two_hour = models.DecimalField()
    

    def __str__(self):
        return f"{self.title}"