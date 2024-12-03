import random
from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from api.models import Order, OrderItem, Product, User
from decimal import Decimal


class Command(BaseCommand):
    help = 'Created applicaion data'


    def handle(self, *args, **kwargs):

        user = User.objects.filter(username='admin').first()

        if not user:
            user = User.objects.create_superuser(
                username='admin',
                password='123456'
            )

        products_list = [
            Product(name="A Scanner Darkly", description=lorem_ipsum.paragraph(), price=Decimal('12.99'), stock=4),
            Product(name="Coffee Machine", description=lorem_ipsum.paragraph(), price=Decimal('70.99'), stock=6),
            Product(name="Velvet Underground & Nico", description=lorem_ipsum.paragraph(), price=Decimal('15.99'), stock=11),
            Product(name="Enter the Wu-Tang (36 Chambers)", description=lorem_ipsum.paragraph(), price=Decimal('17.99'), stock=2),
            Product(name="Digital Camera", description=lorem_ipsum.paragraph(), price=Decimal('350.99'), stock=4),
            Product(name="Watch", description=lorem_ipsum.paragraph(), price=Decimal('500.05'), stock=0),
        ]

        Product.objects.bulk_create(products_list)

        products_obj = Product.objects.all()

        for _ in range(5):
            order = Order.objects.create(user=user)
            no_of_prod_in_order = random.randint(1, 4)

            for product in random.sample(list(products_obj), no_of_prod_in_order):
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=random.randint(1,3)
                )
