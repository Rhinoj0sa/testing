import datetime

from django.contrib import admin
from .models import Product

admin.site.register(Product)
# Register your models here.
# Product.objects.create(name='baseball cap', price='19.99', description='baseball cap description', quantity=2,published_on=datetime.now())
#
