from django.contrib import admin
from .models import Services,Products,Cart,All_Orders,OrderItems,Payments,Reviews,Team,Stores
# Register your models here.
@admin.register(Reviews)
class Reviews(admin.ModelAdmin):
    fields = (("customer"),'review_image','description')

@admin.register(Services)
class Services(admin.ModelAdmin):
    fields = (("service_name"),"service_image","description")

@admin.register(Products)
class Products(admin.ModelAdmin):
    fields = (("product_name","product_brand"),"product_price","category","Target","product_stock","product_image","description")
@admin.register(Cart)
class Cart(admin.ModelAdmin):
    fields=(("user"),'quantity','price','product','session_key')
@admin.register(All_Orders)
class All_Orders(admin.ModelAdmin):
    fields =('customer','shipping_details','mobile','total')
@admin.register(OrderItems)
class Order_Items(admin.ModelAdmin):
    fields=(('order'),'product','price')
@admin.register(Payments)
class Payments(admin.ModelAdmin):
    fields=('customer','amount','mobile')
@admin.register(Team)
class Team(admin.ModelAdmin):
    fields = (('profile_name'), 'profile_occupation', 'quote', 'profile_image')
@admin.register(Stores)
class Stores(admin.ModelAdmin):
    fields = (('city'),'phone_number','email_address','physical_address','office_pic','basic_desc')