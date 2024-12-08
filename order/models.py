from django.db import models
from home.models import product  # lowercase as in your original code

class Order(models.Model):
    Product = models.ForeignKey(product, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    delivery_zone = models.CharField(max_length=100, default='Others')  # Add this line
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Order for {self.full_name} - {self.Product.product_title}"