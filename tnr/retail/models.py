from django.db import models

# Create your models here.
class products(models.Model):
	productid=models.IntegerField(primary_key=True)
	productname=models.CharField(max_length=255)
	productdescription=models.CharField(max_length=255)
	productprice=models.DecimalField(max_digits=10,decimal_places=2)
	productimage=models.ImageField(upload_to='images/')

class customer(models.Model):
	customerid=models.IntegerField(primary_key=True)
	customername=models.CharField(max_length=255)
	customeremail=models.CharField(max_length=255)
	customeraddress=models.CharField(max_length=255)

class orders(models.Model):
	orderid=models.IntegerField(primary_key=True)
	customerid=models.ForeignKey(customer,on_delete=models.CASCADE)
	orderdate=models.DateField(null=True)
	shippingaddress=models.CharField(max_length=255)
	paymentmethod=models.CharField(max_length=255)

class orderdetails(models.Model):
	orderdetailid=models.IntegerField(primary_key=True)
	orderid=models.ForeignKey(orders,on_delete=models.CASCADE)
	productid=models.ForeignKey(products,on_delete=models.CASCADE)
	quantity=models.IntegerField()
	price=models.DecimalField(max_digits=10,decimal_places=2)

class review(models.Model):
	reviewid=models.IntegerField(primary_key=True)
	productid=models.ForeignKey(products,on_delete=models.CASCADE)
	customerid=models.ForeignKey(customer,on_delete=models.CASCADE)
	rating=models.IntegerField()
	text=models.CharField(max_length=255)
