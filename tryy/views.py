from django.shortcuts import render,HttpResponse,redirect
from tryy.models import Product
from tryy.models import Signup
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import stripe
# for payment gateway
from django.conf import settings
from django.urls import reverse
from math import ceil


def index(request):
    products = Product.objects.all()
    n=len(products)
    nslides=n//4+ceil((n/4)-(n//4))
    params={'no_of_slides':nslides,'range':range(nslides),'products':products}
    # context={
    #     "data":[1,2,3,4,5,6,7,8,9,10],
    # }
    
    return render(request,'index.html',params)

def products(request):
    # products = Product.objects.all()
    # n=len(products)
    # nslides=n//4+ceil((n/4)-(n//4))
    # params={'no_of_slides':nslides,'range':range(nslides),'products':products}
    # prod=Product.objects.filter(id=id)
    return render(request, 'products.html')

def signu(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('passsword')
        username=request.POST.get('username')
        signup=Signup(email=email,passsword=password)
        
        myuser=User.objects.create(username=username, email=email, password=password)
        myuser.save()
        signup.save()
        messages.success(request,"your data hase been saved")
    return render(request,'signup.html')

def loginn(request):
    if request.method=='POST':
        usernameee=request.POST.get('uname')
        # email=request.POST.get('mail')
        passworddd=request.POST.get('psw')
        
        user=authenticate(username=usernameee,password=passworddd)
        print("BRRRRRRRR:", user)
        if user is not None:
            login(request,user)
            messages.success(request,"successfully lloged in")
            return redirect('payment')
            
        
        else:
            messages.success(request,"invalid ")
            return render(request,'index.html')
    
    return render(request,'login.html')

def logoutt(request):
    # if request.method=="POST":
    logout(request)
    messages.success(request,"you are successfully loged out")
    return render(request,'products.html')

    return HttpResponse('handellogput')

def paymentt(request):
    stripe.api_key=settings.STRIPE_API_KEY
    session=stripe.checkout.Session.create(payment_method_types=['card'],
            line_items=[{
                'price':'price_1MWPMPSFa0lDu0oS0JLDoNw2',
                'quantity':2,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('products/')),
            cancel_url=request.build_absolute_uri(reverse('login')),)
    context={
        'session_id':session.id,
        'stripe_public_key':settings.STRIPE_PUBLIC_KEY
        }
    return render(request,'payment.html',context)

# error prone zone

    