from django.db import models

class categeroy(models.Model):
    c_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.c_name

class product(models.Model):
    product_id=models.AutoField(primary_key=True)
    catagory_name=models.ForeignKey(categeroy,on_delete=True)
    product_name=models.CharField(max_length=500)
    product_price=models.IntegerField()
    product_image=models.ImageField(upload_to="productGallary")
    def __str__(self):
        return self.product_name

class signupImage(models.Model):
    signup_image=models.ImageField(upload_to="gallary")

class LoginImage(models.Model):
    sign_in=models.ImageField(upload_to="gallary")

class RegisterDetails(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField(primary_key=True)
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    confirm_password=models.CharField(max_length=15)
    def __str__(self):
        return self.name
class CartItems(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    p_id=models.IntegerField()
    def __str__(self):
        return self.name