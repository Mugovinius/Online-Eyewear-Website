from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import uuid
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Services(models.Model):
    service_image = models.ImageField(blank=True, null=True, upload_to="images/")
    service_name = models.CharField(max_length=40)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.service_name

class Products(models.Model):
    product_image = models.ImageField(upload_to="images/")
    product_name = models.CharField(max_length=30)
    product_brand = models.CharField(max_length=30)
    product_price = models.CharField(max_length=20)
    product_stock = models.IntegerField(null=False)
    target = models.CharField(max_length = 20)
    category = models.CharField(max_length=30)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')

    def __str__(self):
        return self.user
class All_Orders(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = PhoneNumberField(null =False,blank=False)
    shipping_details = models.CharField(max_length=50,default="Nairobi, Kenya", editable=True)
    date = models.DateTimeField(auto_now_add=True)
    order_no = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    def __str__(self):
        return f'{self.customer}'
class OrderItems(models.Model):
    order = models.ForeignKey(All_Orders,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1,editable=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_status = models.BooleanField(default=False)
    parcel_arrived_status = models.BooleanField(default=False)
    parcel_collected_status =models.BooleanField(default=False)
    reviewed_status = models.BooleanField(default=False)
    shipping_status = models.CharField(max_length=50, default="Pending Dispatch",editable=True)
    payment_status = models.CharField(max_length=50,default="Pending Confirmation",editable=True)
    def __str__(self):
        return f'{self.product}'
    
class Payments(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    order_no = models.ForeignKey(All_Orders,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    mobile = PhoneNumberField(blank =False,null=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.customer}'
    
class Reviews(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    review_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderItems,on_delete=models.CASCADE)
    review_image = models.ImageField(upload_to="images/")
    description = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.customer}'
    
class Team(models.Model):
    profile_image = models.ImageField(upload_to="images/")
    profile_name = models.CharField(max_length=50)
    profile_occupation = models.CharField(max_length=70)
    quote = models.TextField(max_length=300)

    def __str__(self):
        return self.profile_name
    
class Stores(models.Model):
    city = models.CharField( max_length=50)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField("Email Address")
    physical_address = models.CharField(max_length=80)
    office_pic = models.ImageField(null=True,blank=True, upload_to="images/")
    basic_desc = models.TextField(max_length=200)

    def __str__(self):
        return self.city