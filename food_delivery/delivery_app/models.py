from django.db import models

class FoodOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    restaurant_name = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_address = models.TextField()

    def __str__(self):
        return f"Order #{self.order_id} - {self.customer_name} ({self.food_item})"