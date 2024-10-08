from django.contrib import admin

# Register your models here.
from app1.models import Contact,Home,Order,Userslogin,Cart
admin.site.register(Contact)
admin.site.register(Home)
admin.site.register(Order)
admin.site.register(Userslogin)
admin.site.register(Cart)
