from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.get_all_products),
    path("products/<int:pk>/", views.get_single_product),
    path("products/info/", views.get_products_info),
    path("orders/", views.get_all_orders),
    path("orders/<uuid:pk>/", views.get_single_order),
]