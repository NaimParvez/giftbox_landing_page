from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from home.models import product  # lowercase
from .models import Order
import json

class SubmitOrderView(View):
    def post(self, request, product_slug):
        # Get the product details using the slug
        product_instance = get_object_or_404(product, product_slug=product_slug)
        
        # Extract data from the form
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        delivery_zone = request.POST.get('delivery_zone', 'Others')
        quantity = int(request.POST.get('quantity', 1))

        # Determine delivery charge based on zone
        delivery_charge = 60 if delivery_zone == "Dhaka City Corporation" else 120

        # Calculate the total price
        total_price = (product_instance.product_price * quantity) + delivery_charge

        # Save the order in the database
        Order.objects.create(
            Product=product_instance,
            full_name=full_name,
            phone=phone,
            address=address,
            delivery_zone=delivery_zone,
            quantity=quantity,
            total_price=total_price,
        )
        
        # Redirect to a success page
        return redirect('order_success')

@require_POST
def calculate_total_price(request, product_slug):
    try:
        data = json.loads(request.body)
        quantity = int(data.get('quantity', 1))
        delivery_zone = data.get('delivery_zone', 'Others')

        product_instance = get_object_or_404(product, product_slug=product_slug)

        delivery_charge = 60 if delivery_zone == "Dhaka City Corporation" else 120
        total_price = float((product_instance.product_price * quantity) + delivery_charge)

        return JsonResponse({
            'success': True, 
            'total_price': total_price  # Explicitly convert to float
        })
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'error': str(e)
        }, status=400)