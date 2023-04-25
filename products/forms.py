from django import forms
from django.forms import ModelForm
from .models import Services,Products,Cart,All_Orders,Payments,Reviews, Team, Stores
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
class ServicesForm(ModelForm):
    class Meta:
        model = Services
        fields = ("service_image","service_name","description")

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ("product_name","category", "product_brand","product_price","product_stock","target","product_image","description")

class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ("review_image","description")
        
class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ("quantity",)

class OrdersForm(ModelForm):
    class Meta:
        model = All_Orders
        mobile = PhoneNumberField()
        fields = ("shipping_details","mobile")

class PaymentsForm(ModelForm):
    class Meta:
        model = Payments
        fields = ("amount",)

#create a team form
class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ("profile_name","profile_occupation","profile_image","quote")

#create office form
class StoresForm(ModelForm):
    class Meta:
        model = Stores
        fields = ("city","phone_number","email_address","physical_address","office_pic","basic_desc")