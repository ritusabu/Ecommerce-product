from django.shortcuts import render, redirect
from orders.models import Order, Custumer
from product.models import Category, Offer, Products
from orders.models import ShoppingList
from datetime import datetime
# Create your views here.
def payment(request):
    o= Order.objects.all()
    c= Category.objects.all()
    f = Offer.objects.all()
    raddress= request.GET.get("address","")
    
    # if(request.user.is_authenticated) :
    #     print(request.user.username)
    #     print("user logged he")
    # else:
    #     print("user logged nai he")
    u= request.user.username


    s= ShoppingList.objects.filter(customer__email__exact =u)
    print(len(s))
   
    if len(s) == 0:
        return redirect("/login")
    
        # yaha pe shoping list banai
        # 1 find the cutsomer  current loging he krke
        # 2 create shoping list of that customer
    sum = 0
    total_discount=0
    delivery_charge=0
    total_amount=0
    for p in s[0].products.all():
        sum= sum + p.price
        total_discount= total_discount+(p.price * p.discount)/100
        delivery_charge=delivery_charge+50

        total_amount += p.price -  (p.price * p.discount)/100  
  

        # 50 - 37.5 = 25
     

    total_amount +=  delivery_charge
    # total_amount = ((total_amount - sum )/sum)/100
    print(sum)
    print(total_discount)
    print(delivery_charge)
    print(total_amount)
    print(raddress)

    if raddress != "":
        for p in s[0].products.all():
            o = Order(product=p,delivery_address= raddress,
            delivery_time=datetime(2021,8,1,16),
            custumer= s[0].customer

            )
            o.save()
        s[0].products.clear()
        return redirect('/order')


                
 
    context={
        "orders": o,
        "catagory": c,
        "offer": f,
        "shop_list":s[0],
        "price": sum,
        "total_discount":total_discount,
        "delivery_charge":delivery_charge,
        "total_amount":total_amount


    }
    return render(request, 'cart/payment.html', context)


def addCart(request, id):

    u= request.user.username
    s= ShoppingList.objects.filter(customer__email__exact=u)
    p = Products.objects.get(id = id)
    

    # is s is none then create else 
    if len(s) == 0:
        return redirect("/login")
        
        # class ShoppingListCreateView(ShoppingList):
        #     model =ShoppingList
        #     cart = "cart"
        
        
    else:
        s[0].products.add(p)
        s[0].save()
        print(s[0].products.all())
    
    
    
    print(p)
    if len(s) != 0:
        s[0].products.add(p)
        s[0].save()
        print(s[0].products.all())
    
    return redirect("/detail/{0}/".format(id))


def removeCart(request, id):
    u= request.user.username
    s = ShoppingList.objects.filter(customer__email__exact=u)
    p=Products.objects.get(id = id) #if len(arrayy) != 0: then remove else do nothing...

    if s[0].products.count() !=0:
        s=s[0].products.remove(p)

    return redirect("/payment")

     
