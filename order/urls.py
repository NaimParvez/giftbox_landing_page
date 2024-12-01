from django.urls import path
from django.views.generic import TemplateView
from .views import SubmitOrderView


urlpatterns = [
    path('submit-order/<slug:product_slug>/', SubmitOrderView.as_view(), name='submit_order'),
    path('order-success/', TemplateView.as_view(template_name="order_success.html"), name='order_success'),
]
