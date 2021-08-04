from django.db import models
from django.db.models.base import Model
from store.models import Product

class Cart(models.Model):
    date_added = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.is_active)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.product_name
