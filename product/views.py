from django.shortcuts import render
from product.models import Products, Category, Review, Offer
from orders.models import ShoppingList

# Create your views here.
def home(request):
   
    products = Products.objects.filter(best = True)[:4]
    category = Category.objects.all()
    o = Offer.objects.all()
    u= request.user.username
    s= ShoppingList.objects.filter(customer__email__exact =u)
  
    if len(s) != 0:
        s = s[0]
    else:
        s = None

    context = {
        "products":products,
        "catagory": category ,
        "shop_list":s,
        "offer":o
    }

  
  
    return render(request, "product/home.html",context)

def cart(request,cat_name):
   
    category = Category.objects.all()
    products = Products.objects.filter(category__name__exact=cat_name)
    off =  Offer.objects.all()
    p=[]
    
    for w in products:
        p.append({
            "id":w.pk,
            "name":w.name,
            "price":w.price,
            "image":w.image.url,
            "discount":w.discount,
            "discounted_price":(w.price*w.discount)/100,
            
        })

    
    context = {
        "products":p,
        "catagory": category,
        "offer":off
  
    }

    return render(request, "product/cart.html",context )

def detail(request,id):
    p= Products.objects.get(id=id)
    c=Category.objects.all()
    r= Review.objects.filter(product__id=id)
    o= Offer.objects.all()
    u= request.user.username
    s= ShoppingList.objects.filter(customer__email__exact =u)

   
    
    if len(s) != 0:
        s = s[0]
    else:
        s = None
        
    d={
        "p":p,
        "catagory":c,
        "review":r,
        "offer":o,
        "shop_list":s
    }
    return render(request, "product/product-deaitls.html", d)

def offer(request, off_id):
    catagory=Category.objects.all()
    off = Offer.objects.all()
    o = Offer.objects.get(id = off_id) # muje off_id woh offer do 
    p = o.products.all() # many to many 
    

    print(o.products.all())
    a=[]
    
    for w in p:
        a.append({
            "id":w.pk,
            "name":w.name,
            "price":w.price,
            "image":w.image.url,
            "discount":w.discount,
            "discounted_price":(w.price*w.discount)/100,
            
        })

    context={
        "catagory":catagory,
        "offer":off,
        "products":a
        # key: varnaem
    }
    return render(request, 'product/offer.html', context)

def search(request):
    t= request.GET.get("name", "")     # context.get("products","")

    p= Products.objects.filter(name__contains=t) # list of products jiske name me d ho
    category= Category.objects.all()
    off = Offer.objects.all()
    print(p)
    context={
        "products":p,
        "catasgory":category,
        "offer":off

    }


    return render(request,'product/search.html', context)