from django.contrib import admin
from .models import Producto, Admin, Producto2,Producto3
# Register your models here.

admin.site.register(Producto)
admin.site.register(Producto2)
admin.site.register(Producto3)
admin.site.register(Admin)