from django.shortcuts import get_object_or_404, redirect
from django.views import View
from home.models import product  # lowercase
from .models import Order

# class SubmitOrderView(View):
#     def post(self, request, product_slug):
#         # Get the product details using the slug
#         product_instance = get_object_or_404(product, product_slug=product_slug)  # lowercase product
        
#         # Get the form data
#         full_name = request.POST.get('full_name')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         city = request.POST.get('city')
#         postal_code = request.POST.get('postal_code')
#         quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not provided
        
#         # Calculate the total price (product price + delivery charge)
#         delivery_charge = 50  # Example: Static delivery charge
#         total_price = (product_instance.product_price * quantity) + delivery_charge        
#         # Save the order in the database
#         Order.objects.create(
#             Product=product_instance,  # Use the retrieved product instance
#             full_name=full_name,
#             phone=phone,
#             address=address,
#             city=city,
#             postal_code=postal_code,
#             quantity=quantity,  # Save quantity
#             total_price=total_price,
#         )
        
#         # Redirect to a success page
#         return redirect('order_success')

class SubmitOrderView(View):
    def post(self, request, product_slug):
        product_instance = get_object_or_404(product, product_slug=product_slug)

        # Debugging: Print the POST data
        print(request.POST)

        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not provided

        # Calculate the total price
        delivery_charge = 50
        total_price = (product_instance.product_price * quantity) + delivery_charge

        # Debugging: Print calculated values
        print(f"Quantity: {quantity}, Total Price: {total_price}")

        # Save the order
        Order.objects.create(
            Product=product_instance,
            full_name=full_name,
            phone=phone,
            address=address,
            city=city,
            postal_code=postal_code,
            quantity=quantity,  # Save the correct quantity
            total_price=total_price,
        )

        return redirect('order_success')
