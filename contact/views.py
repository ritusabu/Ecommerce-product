from django.shortcuts import render
from django.http import HttpResponse
from contact.models import Contact
from product.models import Offer, Category, Products

# Create your views here.
def contact(request):
    a= request.POST.get("name", "")
    b= request.POST.get("mail", "")
    c= request.POST.get("text", "")
    o= Offer.objects.all()
    t= Category.objects.all()

    
    if a!="" and b!="" and c!="":
        c=Contact(name=a, email=b, messege=c)
        c.save()
    context={
        "offer":o,
        "catagory":t
    }
    

 
    return render(request, 'contact/contact.html' , context)

def home(request):
    return HttpResponse("E-commerse")