"""tnr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from retail import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('t/',views.sample),
    path('index/',views.home,name="index"),
    path('pro/',views.productions,name="products"),
    path('i/',views.inserted,name="success"),
    path('list/',views.list,name="productlist"),
    path('prodel/<int:K>/',views.productdel,name="productdel"),
    path('cus/',views.customern,name="customer"),
    path('cs/',views.csuccess,name="csuccess"),
    path('clist/',views.customerlist,name="customerlist"),
    path('cdel/<int:p>',views.customerdel,name="customerdel"),
    path('order/',views.order,name="order"),
    path('os/',views.ordersuccess,name="osuccess"),
    path('ol/',views.orderlist,name="orderlist"),
    path('orderdel/<int:p>',views.orderdel,name="orderdel"),
    path('odl/',views.orderdetail,name="orderdetail"),
    path('odllist/',views.orderdetaillist,name="odellist"),
    path('odldel/<int:p>/',views.orderdetaildel,name="orderdetaildel"),
    path('review/',views.reviews,name="review"),
    path('rs/',views.rsuccess,name="rsuccess"),
    path('rlist/',views.reviewlist,name="reviewlist"),
    path('rdel/<int:p>',views.reviewdel,name="reviewdel")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

