from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta

from .models import Customer, Order, Product


def index(request):
    html = """
        <html>
        <head>
            <title>Главная страница</title>
        </head>
        <body>
            <h1>Главная страница</h1>
            <p>Главная страница</p>
        </body>
        </html>
    """
    return HttpResponse(html)


def ordered_products(request, customer_id, days):
    customer = Customer.objects.get(pk=customer_id)
    current_date = timezone.now()
    start_date = current_date - timedelta(days=days)
    products_list = Product.objects.filter(order__customer=customer,
                                           order__order_date__gte=start_date,
                                           order__order_date__lte=current_date).distinct().values('name')

    return render(request, 'hw02app/ordered_items.html', {'products_list': products_list})


def customer_name(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, "hw02app/customer.html", {"customer": customer})
