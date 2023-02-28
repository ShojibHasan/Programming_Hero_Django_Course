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



def search(request):
    get_method = request.GET.copy()
    keywords = get_method.get('keywords') or None
    category = get_method.get('category') or None
    product = Product.objects.all()
    
    if keywords:
        keyword = get_method['keywords']
        product_list = product.filter(description__icontains=keyword)
        
    if category:
        category = get_method['category']
        product_list = product.filter(category__iexact=category)
        
    print("product list: ",product_list)
    
    # if 'name' in get_method:
    #     product = get_method['name']
    #     product_list = product.filter(name__icontains=keyword)
    
    context = {
        'product_list':product_list
    }
    
    return render(request,'search/search_result.html',context)