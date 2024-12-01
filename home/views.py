# from django.shortcuts import render,redirect
# from django.views import generic

# from .models import (
#     product,
#     )


# class Home(generic.TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = product.objects.all()
#         return context

# # Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import product, Slider, Upcoming

class Home(ListView):
    model = product
    template_name = 'index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the active slider and upcoming items
        context['slider'] = Slider.objects.filter(show=True).first()
        context['upcoming'] = Upcoming.objects.filter(show=True).first()
        return context 


class ProductBuyView(TemplateView):
    template_name = "buy_product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch the product using the slug
        product_slug = kwargs.get('product_slug')
        Product = get_object_or_404(product, product_slug=product_slug)
        context['product'] = Product
        return context