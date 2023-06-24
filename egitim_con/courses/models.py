from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    isActive = models.BooleanField()

    def __str__(self):
        return f"{self.title} {self.date}"
    
class Category(models.Model):
    name = models.CharField(max_length=40)
    slug=models.CharField(max_length=50)
    