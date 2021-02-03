"""ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from contact.views import contact,home
from product.views import home, cart, detail, offer, search

from django.conf import settings
from django.conf.urls.static import static
from authln.views import authln, register,lo
from orders.views import order
from cart.views import payment, addCart, removeCart


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('cart/<cat_name>/', cart, name="cart"),
    path('detail/<id>/', detail, name="detail"),
    path('login/', authln, name='authln'),
    path('offers/<off_id>/', offer, name="offer"),
    path('search/' , search, name="search"),
    path('register/', register, name="register"),
    path('logout/', lo, name="logout"),
    path('order/', order, name="order"),
    path('payment/',payment,name="payment" ),
    path('addcard/<id>/', addCart, name="addCard"),
    path('removeCrad/<id>/', removeCart, name="removeCard")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

