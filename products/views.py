from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""
A view that displays all products
Paginate is filtered on product name

"""


def all_products(request):
    product_list = Product.objects.filter().order_by('name')
    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})


"""
A view that displays only the Guitars
Paginate is filtered on product name

"""


def guitars(request):
    product_list = Product.objects.filter(category='guitars').order_by('name')
    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "guitars.html", {"products": products})


"""
A view that displays only the Keyboards
Paginate is filtered on product name

"""


def keyboards(request):
    product_list = Product.objects.filter(
        category='keyboards').order_by('name')
    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "keyboards.html", {"products": products})


"""
A view that displays only the Percussion
Paginate is filtered on product name

"""


def percussion(request):
    product_list = Product.objects.filter(
        category='percussion').order_by('name')
    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "percussion.html", {"products": products})


"""
A view that displays additional detail on each product in a new page

"""


def product_detail(request, pk):
    products = Product.objects.filter(pk=pk)
    product = get_object_or_404(Product, pk=pk)

    return render(request, "product_detail.html", {'product': product,
                                                   'products': products})
