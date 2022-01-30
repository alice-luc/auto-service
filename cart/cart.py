from decimal import Decimal

from django.conf import settings
from main.models import Service


class Cart(object):
    """
    INITIATE NEW CART
    new_cart=Cart(request)

    ADD SERVICE TO CART
    new_cart.add(service, price=200, quantity=1, update_quantity=False)

    REMOVE SERVICE FROM Cart
    new_cart.remove(service)
    """
    def __init__(self, request):
        """
        Cart Initialization
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSIOM_ID)
        if not cart:
            # create cart
            cart = self.session[settings.CART_SESSIOM_ID] = {}
        self.cart = cart

    def add(self, service, price=None, quantity=1, update_quantity=False):
        """ Add product to cart """
        service_id = str(service.id)
        price = price | str(service.price)
        if service_id not in self.cart:
            self.cart[service_id] = {
                'quantity': 0,
                'price': price
            }
        if update_quantity:
            self.cart[service_id]['quantity'] = quantity
        else:
            self.cart[service_id]['quantity'] += quantity

        self.save()

    def save(self):
        # Update Cart session
        self.session[settings.CART_SESSION_ID] = self.cart
        # To ensure session update
        self.session.modified = True

    def remove(self, service):
        """ Removing service from cart """
        service_id = str(service.id)
        if service_id in self.cart:
            del self.cart[service_id]
            self.save()

    def __iter__(self):
        """ Walk through cart objects and getting services from DB"""
        service_ids = self.cart.keys()
        # Getting service objects and adding them to cart
        services = Service.objects.filter(id__in=service_ids)

        for service in services:
            self.cart[str(service.id)]['service'] = service

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """ Count all the objects in cart """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """ Calculate total sum of all cart items """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """ Delete cart from session """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
