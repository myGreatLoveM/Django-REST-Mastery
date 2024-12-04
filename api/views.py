from django.shortcuts import get_object_or_404
from django.db.models import Max, Min, Avg
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product, Order
from .serializers import OrderSerializer, ProductSerializer, ProductInfoSerializer



class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(stock__gt=0)
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer


class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'order_id'


class UserOrderDetailAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# @api_view(['GET'])
# def get_all_products(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def get_single_product(request, pk):
#     # product = Product.objects.get(id=pk)
#     # product = Product.objects.get(pk=pk)
#     product = get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)


# @api_view(['GET'])
# def get_all_orders(request):
#     orders = Order.objects.prefetch_related("items__product")
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def get_single_order(request, pk):
#     # order = get_object_or_404(Order, pk=pk)
#     order = Order.objects.prefetch_related("items__product").get(pk=pk)
#     serializer = OrderSerializer(order)
#     return Response(serializer.data)


@api_view(['GET'])
def get_products_info(request):
    products = Product.objects.all()
    price_info = products.aggregate(
        max_price=Max('price'),
        min_price=Min('price'),
        avg_price=Avg('price'),
    )
    serializer = ProductInfoSerializer({
        'products': products,
        'no_of_product': len(products),
        'max_price': price_info.get('max_price'),
        'min_price': price_info.get('min_price'),
        'avg_price': price_info.get('avg_price'),
    })
    return Response(serializer.data)







