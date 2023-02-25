from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
# Create your views here.


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            # email.lower()
            
            user = authenticate(request,email=email, password=password)
            if user:
                login(request,user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid Email or Password.')
                # messages.error(request,'Invalid Email or Password')
    return render(request,'accounts/login.html')


def registration(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST' and request.FILES['image']:
            first_name = request.POST.get('first_name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address = request.POST.get('address')
            image = request.FILES['image']
            
            email_exists = User.objects.filter(email=email)
            if not email_exists:
                user = User.objects.create_user(first_name=first_name,phone=phone,email=email,password=password,address=address,image=image)
                user.is_active=True
                user.save()
                messages.success(request,'Registration Sucessfull')
                return render(request,'accounts/login.html')
            else:
                messages.error(request,'Email already Taken')
    return render(request,'accounts/registration.html')

@login_required
def logout(request):
    django_logout(request)
    return redirect('index')