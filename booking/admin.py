from django.contrib import admin
from .models import Consumer, Order, Invoice

admin.site.register(Consumer)
admin.site.register(Order)
admin.site.register(Invoice)
