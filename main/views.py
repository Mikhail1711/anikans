from django.shortcuts import render
from django.db.models import Q, CharField
from django.db.models.functions import Cast
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from goods.models import Categories, Titles, Heroes, Products
from journal.models import Supplies, Sales


def index(request):
    
    category_id = request.GET.get('category')
    title_id = request.GET.get('title')
    hero_id = request.GET.get('hero')
    barcode = request.GET.get('barcode')
    audit = request.GET.get('checkboxAudit') is not None
    products = []
    
    if 'search' in request.GET:
        products = Products.objects.all()

        if category_id:
            products = products.filter(category_id=category_id)
        if title_id:
            products = products.filter(hero__title_id=title_id)
        if hero_id:
            products = products.filter(hero_id=hero_id)
        if barcode:
            products = products.annotate(
                item_str=Cast('item', CharField()),
                description_str=Cast('description', CharField())
            )
            products = products.filter(
            Q(barcode__endswith=barcode) | 
            Q(item_str__iendswith=barcode.lower()) | 
            Q(description_str__icontains=barcode.lower())
            )
        if audit:
            products = products.filter(quantity__lt=0)

    context = {
        'categories': Categories.objects.all(),
        'titles': Titles.objects.all(),
        'heroes': Heroes.objects.all(),
        'products': products,
    }
    return render(request, 'main/index.html', context)


@csrf_exempt
def add_to_list(request):
    item_id = request.POST.get('item_id')
    item = Products.objects.get(id=item_id)
    quantity = request.POST.get('quantity')
    to_list = request.POST.get('to_list')
    if to_list == "Supplies":
        cart_item, created = Supplies.objects.get_or_create(product=item)
        cart_item.quantity += int(quantity)
        cart_item.save()
    if to_list == "Sales":
        cart_item, created = Sales.objects.get_or_create(product=item)
        cart_item.quantity += int(quantity)
        cart_item.save()
    return JsonResponse({'status': 'success'})
