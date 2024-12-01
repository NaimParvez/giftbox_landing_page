# from django.urls import path
# from . import views

# urlpatterns = [
#     path('',Home.as_view(),name='index'),
# ]
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import Home
from .views import ProductBuyView

urlpatterns = [
    path('', Home.as_view(), name='index'),
   path('buy/<slug:product_slug>/', ProductBuyView.as_view(), name='buy_product'),
]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL,document_root =settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)