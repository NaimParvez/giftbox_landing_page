from django.db import models
from django.utils.text import slugify

class product(models.Model):
    product_title = models.CharField(max_length=50) 
    product_slug = models.SlugField(max_length=50, unique=True, blank=True)# Allow blank initially
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_img = models.ImageField(upload_to='product_image')
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True) 
    created_data = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generate slug only if it doesn't already exist
        if not self.product_slug:
            self.product_slug = slugify(self.product_title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.product_title
    
class Slider(models.Model):
    title = models.CharField(max_length=50)
    banner = models.ImageField(upload_to='slider_image')
    show = models.BooleanField(default=False)
    created_data = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.show:
            # Set all other sliders' `show` to False
            Slider.objects.exclude(id=self.id).update(show=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Upcoming(models.Model):
    title = models.CharField(max_length=50)
    banner = models.ImageField(upload_to='upcoming_image')
    discount = models.CharField(max_length=50)
    show = models.BooleanField(default=False)
    created_data = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.show:
            # Set all other upcoming items' `show` to False
            Upcoming.objects.exclude(id=self.id).update(show=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
