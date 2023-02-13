from django.contrib import admin
from .models import Funko, Order, Address, OrderFunko

# Register your models here.

admin.site.register(Funko)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(OrderFunko)



