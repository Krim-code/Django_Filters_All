from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(default=0.0)
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='products')
    color = models.CharField(max_length=50, choices=[
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
    ])

    def __str__(self):
        return self.name