from django.contrib import admin
from .models import Cart,Category,MenuItem,OderItem,Order
# Register your models here.

admin.site.register([Cart,Category,MenuItem,OderItem,Order])