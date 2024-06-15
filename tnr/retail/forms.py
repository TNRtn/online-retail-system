from .models import products,customer,orders,orderdetails,review
from django import forms


class Aform(forms.ModelForm):
	class Meta:
		model=products
		fields=["productid","productname","productdescription","productprice","productimage"]
		widgets={
		"productid":forms.NumberInput(
			attrs={"class":"form-control my-2","placeholder":"Product ID"
			}),
		"productname":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"Product Name"
			}),
		"productdescription":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"description"
			}),
		"productprice":forms.NumberInput(
			attrs={"class":"form-control my-2","placeholder":"Price","step":0.25
			}),
		"productimage":forms.ClearableFileInput(
			attrs={"class":"form-control my-2","type":"file","placeholder":"Image"
			})
		}
	def __init__(self, *args, **kwargs):
		super(Aform, self).__init__(*args, **kwargs)
		self.fields['productimage'].required = True

class Bform(forms.ModelForm):
	class Meta:
		model=customer
		fields=["customerid","customername","customeremail","customeraddress"]
		widgets={
		"customerid":forms.NumberInput(
			attrs={"class":"form-control my-2","placeholder":"customer ID"
			}),
		"customername":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"customer Name"
			}),
		"customeremail":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"email"
			}),
		"customeraddress":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"address"
			})
		
		}

class Cform(forms.ModelForm):
	class Meta:
		model=orders
		fields=["orderid","customerid","orderdate","shippingaddress","paymentmethod"]
		widgets={
		"orderid":forms.NumberInput(
			attrs={"class":"form-control my-2","placeholder":"Order Id"
			}),
		"customerid":forms.Select(
			attrs={"class":"form-control my-2","placeholder":"customer id"
			}),
		"orderdate":forms.DateInput(
			attrs={"class":"form-control my-2","type":"Date","placeholder":"orderdate"
			}),
		"shippingaddress":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"address"
			}),
		"paymentmethod":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"payment method"
			})
		}

class Dform(forms.ModelForm):
	class Meta:
		model=orderdetails
		fields=["orderdetailid","orderid","productid","quantity","price"]
		widgets={
		"orderdetailid":forms.NumberInput(
			attrs={"class":"form-control my-2","placeholder":"orderdetail Id"
			}),
		"orderid":forms.Select(
			attrs={"class":"form-control my-2","placeholder":"Order ID"
			}),
		"productid":forms.Select(
			attrs={"class":"form-control my-2","placeholder":"Product ID"
			}),
		"quantity":forms.NumberInput(
			attrs={"class":"form-control my-2","placeholder":"Quantity"
			}),
		"price":forms.NumberInput(
			attrs={"class":"form-control my-2","placeholder":"Price","step":0.25
			})
		}


class Eform(forms.ModelForm):
	class Meta:
		model=review
		fields=["reviewid","productid","customerid","rating","text"]
		widgets={
		"reviewid":forms.NumberInput(
			attrs={"class":"form-control my-2","placeholder":"Review Id"
			}),
		"productid":forms.Select(
			attrs={"class":"form-control my-2","placeholder":"Product ID"
			}),
		"customerid":forms.Select(
			attrs={"class":"form-control my-2","placeholder":"Customer ID"
			}),
		"rating":forms.NumberInput(
			attrs={"class":"form-control my-2","placeholder":"Rating(1-5)"
			}),
		"text":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"comments"
			})
		}

