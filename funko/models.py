from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_countries.fields import CountryField


class Funko(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="funko/static/images/", default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_add_to_cart(self):
        return reverse("add_to_cart", kwargs={"funko_id": self.id})

    def get_remove_from_cart(self):
        return reverse("remove_from_cart", kwargs={"funko_id": self.id})


class OrderFunko(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    funko = models.ForeignKey(Funko, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.funko.name}"

    def get_total_price(self):
        return self.funko.price * self.quantity


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    building = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = CountryField()

    def __str__(self):
        return f"{self.building}{self.street}, {self.city}, {self.state}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_no = models.IntegerField(blank=True, null=True)
    order_date = models.DateField(auto_now_add=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderFunko)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
