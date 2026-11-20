# EX02 - Django ORM Web Application
# Date: 20/11/2026
# AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).

# DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 orders

# PROGRAM
```
//admin.py

from django.contrib import admin
from .models import FoodOrder

@admin.register(FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','customer_name','restaurant_name','food_item','quantity','total_price')

```
```
//models.py

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

```

# OUTPUT
<img width="1920" height="1080" alt="Screenshot (31)" src="https://github.com/user-attachments/assets/ba956d15-39b1-472f-9435-1630215a451b" />


# RESULT
Thus the program for creating a database using ORM hass been executed successfully.
