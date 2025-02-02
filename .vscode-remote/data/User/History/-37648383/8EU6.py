from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration_choices = [
        (30, "30 - €55"),
        (60, "60 - €80"),
        (30, "120 - €110"),
    ]
    duration = models.IntegerField(choices=duration_choices)

    def __str__(self):
        rerurn f"{self.title} ({self.get_duration_display()})"