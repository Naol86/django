from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Feature
# Create your views here.

def index(request):
    feature = Feature.objects.all()
    return render(request,'index.html',{'feature': feature})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['EMAIL']
        password = request.POST['PASSWORD']
        password2 = request.POST['PASSWORD2']
        
        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already used.")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"The user already exist.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"passwords are not the same")
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['PASSWORD']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'credentials invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
    
    
    
def counter(request):
    text = request.POST['text']
    amount_of_word = len(text.split())
    return render(request,'counter.html',{'amount': amount_of_word })





