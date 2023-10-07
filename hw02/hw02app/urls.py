from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:customer_id>/<int:days>/', views.ordered_products, name='ordered_products'),
    path('<int:customer_id>/', views.customer_name, name='customer_name'),
]