from django.db import models

# Create your models here.

from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50, choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Bird', 'Bird'), ('Other', 'Other')])
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='animal_images/')
    is_adopted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

