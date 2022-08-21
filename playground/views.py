from decimal import Decimal
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Value, ExpressionWrapper, F, DecimalField
from django.db.models.aggregates import Count, Min, Max, Sum, Avg
from store.models import Product
from store.models import Customer
from store.models import Collection
from store.models import Order
from store.models import OrderItem
from store.models import Promotion
from tags.models import TaggedItem
from django.contrib.contenttypes.models import ContentType

def say_hello(request):
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(discounted_price = discounted_price)

    return render(request, 'hello.html', {'name': 'Mudassir'})
