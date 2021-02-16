from django.shortcuts import render
from product.models import Products, Category, Review, Offer
from orders.models import ShoppingList, Order

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
    u= request.user.username
    s= ShoppingList.objects.filter(customer__email__exact =u)
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
    if len(s) != 0:
        s = s[0]
    else:
        s = None

    
    context = {
        "products":p,
        "catagory": category,
        "offer":off,
        "shop_list":s,
  
    }

    return render(request, "product/cart.html",context )

def detail(request,id):
    p= Products.objects.get(id=id)
    c=Category.objects.all()
    r= Review.objects.filter(product__id=id).order_by("-pk")
    o= Offer.objects.all()
    u= request.user.username
    s= ShoppingList.objects.filter(customer__email__exact =u)
    


    is_review = False
    if request.user.is_authenticated:
    
        product_found_in_order =  Order.objects.filter(product__pk = p.pk)
        if len(product_found_in_order) != 0:
            is_review = True
            review = request.GET.get("input-review","")
            if review != "":
                rr = Review(messege = review,product = p)
                rr.save()
    review = request.GET.get("input-review","")
    

   
    
    if len(s) != 0:
        s = s[0]
    else:
        s = None

    a= {
            "id":p.pk,
            "name":p.name,
            "price":p.price,
            "image":p.image.url,
            "discount":p.discount,
            "discounted_price":(p.price*p.discount)/100,
            
        }
    



    d={
        "p":a,
        "catagory":c,
        "review":r,
        "offer":o,
        "shop_list":s,
        "is_review":is_review
    }
    return render(request, "product/product-deaitls.html", d)

def offer(request, off_id):
    catagory=Category.objects.all()
    off = Offer.objects.all()
    o = Offer.objects.get(id=off_id) # muje off_id woh offer do 
    p = o.products.all() # many to many 
    u= request.user.username
    s= ShoppingList.objects.filter(customer__email__exact =u)

    if len(s) != 0:
            s = s[0]
    else:
        s = None
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
        "products":a,
        "shop_list":s
        # key: varnaem
    }
    return render(request, 'product/offer.html', context)

def search(request):
    t= request.GET.get("name", "")     # context.get("products","")

    p= Products.objects.filter(name__contains=t) # list of products jiske name me d ho
    category= Category.objects.all()
    off = Offer.objects.all()
    u= request.user.username
    s= ShoppingList.objects.filter(customer__email__exact =u)
    if len(s) != 0:
            s = s[0]
    else:
        s = None
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
        "products":a,
        "catagory":category,
        "offer":off,
        "shop_list":s

    }


    return render(request,'product/search.html', context)