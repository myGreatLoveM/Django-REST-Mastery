from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductListAPIView.as_view()),
    path("products/<int:product_id>/", views.ProductDetailAPIView.as_view()),
    path("products/info/", views.get_products_info),
    path("orders/", views.OrderListAPIView.as_view()),
    path("orders/<uuid:order_id>/", views.OrderDetailAPIView.as_view()),
    path("user-orders/", views.UserOrderDetailAPIView.as_view()),
]