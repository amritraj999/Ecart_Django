from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from app1.models import Contact
# Create your views here.
def home(request):
    #return HttpResponse("home")
    return render(request,'index.html')

def products(request):
    #return HttpResponse("products")
    return render(request,'products.html')
        
def about(request):
    #return HttpResponse("about")
    return render(request,'about.html') 

def contact(request):
    #return HttpResponse("contact")
    return render(request,'contact.html')
    
def account(request):
    #return HttpResponse("account")
    return render(request,'account.html')

def accountform(request):

    if request.method=="POST":
        username=request.POST.get("username")
        
        password=request.POST.get("password")
        usera=authenticate(request , username=username,password=password)
        if usera is not None:
            return render(request,"userhome")
        else:
            return render(request,"account.html",{'msg':"Sorry!!! Wrong Username or Password"})


def registeruser(request):
    return render(request,"account.html")

def registerform(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=User.objects.create_user(username=username,password=password, email=email)
        user.save()
        return render(request,"account.html",{'msg':"User Registered"})

def contactform(request):
    if request.method=="POST":
        email=request.POST.get("email")
        name=request.POST.get("name")
        message=request.POST.get("message")
        contact=Contact(name=name, email=email, message=message)
        contact.save()

        return render(request,"contact.html",{'msg':'Query Under Process'})

