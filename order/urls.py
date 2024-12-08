from django.urls import path
from django.views.generic import TemplateView
from .views import SubmitOrderView
from . import views

urlpatterns = [
    path('submit-order/<slug:product_slug>/', SubmitOrderView.as_view(), name='submit_order'),
    path('calculate-total-price/<slug:product_slug>/', views.calculate_total_price, name='calculate_total_price'),
    path('order-success/', TemplateView.as_view(template_name="order_success.html"), name='order_success'),
]
