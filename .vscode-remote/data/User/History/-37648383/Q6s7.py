from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    half_hour = models.IntegerField()
    one_hour = models.IntegerField()
    
    

    def __str__(self):
        return f"{self.title}"