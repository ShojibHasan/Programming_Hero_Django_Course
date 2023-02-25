from django.shortcuts import render
from django.http import HttpResponse
from .models import Slider,Product
# Create your views here.



def index(request):
    slider = Slider.objects.all()
    
    product = Product.objects.all().order_by('-date_added')[:8]
    context ={
        'slider': slider,
        'product': product
    }
    return render(request,'home/index.html',context)


def single_product_details(request,id):
    single_product = Product.objects.get(id=id)
    context={
        'single_product':single_product
    }
    return render(request,'product/single_product.html',context)

def product(request):
    product = Product.objects.all()
    return HttpResponse(product)



