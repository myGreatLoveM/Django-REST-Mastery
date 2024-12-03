from django.shortcuts import get_object_or_404
from django.db.models import Max, Min, Avg
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Order
from .serializers import OrderSerializer, ProductSerializer, ProductInfoSerializer


@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_product(request, pk):
    # product = Product.objects.get(id=pk)
    # product = Product.objects.get(pk=pk)
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    serializer = OrderSerializer(order)
    return Response(serializer.data)


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







