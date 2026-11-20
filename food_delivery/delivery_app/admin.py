from django.contrib import admin
from .models import FoodOrder

@admin.register(FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_name', 'restaurant_name', 'food_item', 'quantity', 'total_price')