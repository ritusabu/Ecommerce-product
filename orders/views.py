from django.shortcuts import render
from product.models import Category, Offer, Products
from orders.models import Order, ShoppingList
from authln.models import Custumer
# Create your views here.
def order(request):
    category = Category.objects.all()
    off =  Offer.objects.all()
    # find a order of customer name contains r
    c = Custumer.objects.filter(email__exact= request.user.username)
    o= Products.objects.all()
    porder = Order.objects.filter(custumer__email__contains=c[0].email)
   
    u= request.user.username
    s= ShoppingList.objects.filter(customer__email__exact =u)
   

    # a = [1,23,4,54,5]
    # a[0] = 1
    # a[1] = 23
    # a[2] = 4
    context = {

        "catagory": category,
        "offer":off,
        "orders":porder,
        "shop_list":s[0],
        "order":o
        

    }

    return render(request, 'orders/orders.html', context)