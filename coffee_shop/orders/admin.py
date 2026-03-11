from django.contrib import admin
from .models import Order, OrderProduct


# Register your models here.
class orderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [orderProductInline]


admin.site.register(Order, OrderAdmin)
