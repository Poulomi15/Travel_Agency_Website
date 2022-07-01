from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable1":"  This is sent",
        "variable2":"  This is accepted"
    }
    return render (request,'index.html',context)
    # return HttpResponse("This is Home Page")

def about(request):
   return render (request,'about.html')

def services(request):
    return render (request,'service.html')
    
def aroundcity(request):
    return render (request,'aroundcity.html')

def aroundstate(request):
    return render (request,'aroundstate.html')

def aroundcountry(request):
    return render (request,'aroundcountry.html')

def aroundcontinent(request):
    return render (request,'aroundcontinent.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phno=phno,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your details has successfully added.")
        
    return render (request,'contact.html')



