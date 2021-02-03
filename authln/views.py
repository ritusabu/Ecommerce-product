from django.shortcuts import render, redirect
from authln.models import Authln, Custumer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from orders.models import ShoppingList

def lo(request):
    logout(request)
    return redirect("/")
# Create your views here.
def authln(request):
    wemail= request.POST.get("email", "")
    wpassword= request.POST.get("password", "")
    u = authenticate(username= wemail,password=wpassword) #check krti datase me user he ki nai 
    if u is not None:
        print(wpassword,wemail)
        print(u)
        r = login(request,u)
        print(r)
        return redirect("/")
   


    return render(request, 'authln/login.html')

def register(request):
    # varname = value
    # POST- private data
    rname = request.POST.get("name", "")
    raddress = request.POST.get("address", "")
    rmobile = request.POST.get("mobile", "")
    remail = request.POST.get("email", "")
    rpassword = request.POST.get("password", "")
    rcity = request.POST.get("city", "")
    rstate = request.POST.get("state", "")


    #     x=Custumer(name=r,address=raddress)
    #     x.save()
    if rname != '':
        c = Custumer(name=rname, address=raddress, 
        phone=rmobile, email=remail, 
        password=rpassword, city=rcity, state=rstate)
        c.save()
        u = User.objects.create_user(username=remail,password=rpassword)
        u.save()
        ss= ShoppingList(customer=c)
        ss.save()
        return redirect('/login/')

   
    return render(request, 'authln/register.html')