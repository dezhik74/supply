from django.contrib import admin

from .models import Orders, OrderItems, OrderMedia, Invoices, Delivers, DeliverItems

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderMedia)
class OrderMediaAdmin(admin.ModelAdmin):
    pass


@admin.register(Invoices)
class InvoicesAdmin(admin.ModelAdmin):
    pass


@admin.register(Delivers)
class DeliversAdmin(admin.ModelAdmin):
    pass


@admin.register(DeliverItems)
class DeliverItemsAdmin(admin.ModelAdmin):
    pass

