from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('product_details/<int:id>',views.single_product_details,name='single_product_details')
    # path('product',views.product,name='product')
]