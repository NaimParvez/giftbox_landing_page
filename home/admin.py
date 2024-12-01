from django.contrib import admin

# Register your models here.
from .models import(
    product,
    Slider,
    Upcoming,
)

admin.site.register(product)
admin.site.register(Slider)
admin.site.register(Upcoming)

