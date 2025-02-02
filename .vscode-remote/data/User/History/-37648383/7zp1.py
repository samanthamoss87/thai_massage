from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def get_prices(self):
        return {
            "30 min": 55,
            "60 min": 80,
            "120 min": 110
        }
    

    def __str__(self):
        return f"{self.title}"