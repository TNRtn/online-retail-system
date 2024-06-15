from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import products,customer,orders,orderdetails,review
from .forms import Aform,Bform,Cform,Dform,Eform

# Create your views here.
def sample(request):
	return HttpResponse("tnr")
def home(request):
	return render(request,'tnr/index.html')
def productions(request):
	if request.method=="POST":
		g=Aform(request.POST,request.FILES)
		if g.is_valid():
			g.save()
			return redirect('success')
		else:
			print(g.errors)
		
	g=Aform()
	return render(request,'tnr/products.html',{'k':g})
def inserted(request):
	return render(request,'tnr/insert.html')

def list(request):
	a=products.objects.all()
	return render(request,'tnr/listofproducts.html',{'e':a})

def productdel(request, K):
    n = products.objects.get(productid=K)
    if request.method == "POST":
        n.delete()
        return redirect('productlist')
    return render(request, 'tnr/productdel.html', {'z': n})

def customern(request):
	if request.method=="POST":
		g=Bform(request.POST)
		if g.is_valid():
			g.save()
			return redirect('csuccess')
		else:
			print(g.errors)
		
	g=Bform()
	return render(request,'tnr/customer.html',{'k':g})

def csuccess(request):
	return render(request,'tnr/csuccess.html')
def customerlist(request):
	b=customer.objects.all()
	return render(request,'tnr/customerlist.html',{'e':b})

def customerdel(request,p):
	n = customer.objects.get(customerid=p)
	if request.method == "POST":
		n.delete()
		return redirect('customerlist')
	return render(request,'tnr/customerdel.html',{'z':n})
def order(request):
	if request.method=="POST":
		g=Cform(request.POST)
		if g.is_valid():
			g.save()
			return redirect('osuccess')
		else:
			print(g.errors)
		
	g=Cform()
	return render(request,'tnr/order.html',{'k':g})

def ordersuccess(request):
	return render(request,'tnr/osuccess.html')

def orderlist(request):
	b=orders.objects.all()
	return render(request,'tnr/orderlist.html',{'e':b})

def orderdel(request,p):
	n = orders.objects.get(orderid=p)
	if request.method == "POST":
		n.delete()
		return redirect('orderlist')
	return render(request,'tnr/orderdel.html',{'z':n})

def orderdetail(request):
	if request.method=="POST":
		g=Dform(request.POST)
		if g.is_valid():
			g.save()
			return redirect('orderdetail')
		else:
			print(g.errors)
		
	g=Dform()
	return render(request,'tnr/orderdetails.html',{'k':g})

def orderdetaillist(request):
	c=orderdetails.objects.all()
	return render(request,'tnr/orderdetaillist.html',{'e':c})

def orderdetaildel(request,p):
	n = orderdetails.objects.get(orderdetailid=p)
	if request.method == "POST":
		n.delete()
		return redirect('odellist')
	return render(request,'tnr/orderdetaildel.html',{'z':n})

def reviews(request):
	if request.method=="POST":
		g=Eform(request.POST)
		if g.is_valid():
			g.save()
			return redirect('rsuccess')
		else:
			print(g.errors)
		
	g=Eform()
	return render(request,'tnr/review.html',{'k':g})

def rsuccess(request):
	return render(request,'tnr/rsuccess.html')

def reviewlist(request):
	c=review.objects.all()
	return render(request,'tnr/reviewlist.html',{'e':c})

def reviewdel(request,p):
	n = review.objects.get(reviewid=p)
	if request.method == "POST":
		n.delete()
		return redirect('reviewlist')
	return render(request,'tnr/reviewdel.html',{'z':n})



