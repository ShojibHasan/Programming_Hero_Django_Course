from django.shortcuts import render
from django.http import HttpResponse
from .models import Slider,Product
# Create your views here.



def index(request):
    slider = Slider.objects.all()
    
    product = Product.objects.all()
    context ={
        'slider': slider,
        'product': product
    }
    return render(request,'home/index.html',context)


# def product(request):
#     product = Product.objects.all()
#     return HttpResponse(product)


