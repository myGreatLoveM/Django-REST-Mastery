from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.get_all_products),
    path("products/<int:pk>/", views.get_single_product)
]