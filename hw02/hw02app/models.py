from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, phone: {self.phone}, address: {self.address}, ' \
               f'date: {self.date}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Name: {self.name}, description: {self.description}, price: {self.price}, quantity: {self.quantity},' \
               f' date: {self.date}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer: {self.customer}, products: {", ".join(str(product) for product in self.products.all())}, ' \
               f'total_price: {self.total_price}, order_date: {self.order_date}'
