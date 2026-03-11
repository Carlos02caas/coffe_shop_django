from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

from products.models import Product


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)

    IVA_RATE = Decimal("0.16")

    def __str__(self):
        return f"order {self.id} by {self.user}"

    @property
    def total(self):
        return sum(item.total_price for item in self.orderproduct_set.all())

    @property
    def subtotal(self):
        return self.total / (Decimal("1.16"))

    @property
    def iva(self):
        return self.total - self.subtotal


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"Order {self.order} of {self.product} with quantity {self.quantity}"
