from django.shortcuts import render
from .models import *


priceList = [
    {'id':1, 'name':'Dưới 50', 'max':5},
    {'id':2, 'name':'Từ 50 đến 100','min':5, 'max':10},
    {'id':3, 'name':'Trên 100','min':10},
]

# Create your views here.
def index(request):
    name = request.GET.get('name', '')
    categoryId = request.GET.get('categoryId')
    categoryList = Category.objects.all()
    productList = Product.objects.filter(name__icontains=name) # tim kiem theo tu khoa k phan biet chu hoa va thuong
    print(productList)
    categoryId = int(categoryId) if categoryId else None
    if categoryId:
        productList = productList.filter(category__id=categoryId)

    priceId = request.GET.get('priceId')
    priceId = int(priceId) if priceId else None
    price = priceList[priceId-1] if price or None
    minPrice, maxPrice = price.get('min'), price.get('max')
    
    if minPrice: productList = productList.filter(price__gte=minPrice)
    if maxPrice: productList = productList.filter(price__lte=maxPrice)
    
    context = { 'productList':productList, 
                'name':name,
                'categoryList':categoryList, 
                'categoryId':categoryId, 
                'priceList':priceList,
                'priceId': priceId,
                } #bien giu trang thai
    return render(request, 'index.html', context)

def viewProductDetail(request, pk):
    product = Product.objects.get(pk=pk) #se tao loi khi k co key
    context = {'product':product}
    return render(request, 'product.html', context)