from rest_framework import serializers
from .models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'stock'
        )

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than 0"
            )
        return value

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'price',
            'stock',
            'description',
        )

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Stock must be greater than or equal to 0"
            )
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than 0"
            )
        return value
    
    


class OrderItemSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(read_only=True)
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        source='product.price'
    )
    
    class Meta:
        model = OrderItem
        fields = (
            'product_name', 
            'product_price', 
            'quantity',
            'subtotal'
        )


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='total_order_amount')

    def total_order_amount(self, obj):
        order_items = obj.items.all()
        return sum(order_item.subtotal for order_item in order_items)

    class Meta:
        model = Order
        fields = (
            'order_id',
            'user',
            'status',
            'created_at',
            'items',
            'total_price'
        )


class ProductInfoSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    no_of_product = serializers.IntegerField()
    max_price = serializers.FloatField()
    min_price = serializers.FloatField()
    avg_price = serializers.FloatField()