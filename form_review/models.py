from django.db import models

# Create your models here.
class Review(models.Model):
    user_name = models.CharField(max_length=20)
    feedback = models.TextField()
    
    def __str__(self):
        return f'user_name is {self.user_name}'