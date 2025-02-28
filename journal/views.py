from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from goods.models import Categories, Titles, Heroes, Products
from journal.models import Journal, Supplies, Sales


def history_view(request):
    sum_of_operations = 0
    for each in Journal.objects.all():
        sum_of_operations += each.total_sum()
    money = Products.objects.get(barcode="0000000000000")

    context = {
        'categories': Categories.objects.all(),
        'titles': Titles.objects.all(),
        'heroes': Heroes.objects.all(),
        'journal': Journal.objects.all(),
        'money': money.quantity,
        'sum': sum_of_operations,
    }
    return render(request, 'journal/history.html', context)


def adding_view(request):
    context = {
        'categories': Categories.objects.all(),
        'titles': Titles.objects.all(),
        'heroes': Heroes.objects.all(),
        'supplies': Supplies.objects.all(),
    }
    return render(request, 'journal/adding.html', context)


@csrf_exempt
def adding_confirm(request):
    data = json.loads(request.body.decode('utf-8'))
    cart_data = data.get('cart_data')

    for item in cart_data:
        item_id = item.get('itemId')
        cart_item = Supplies.objects.get(id=item_id)
        cart_item.quantity = int(item.get('quantity'))
        cart_item.save()

    sum_of_operations = 0
    for item in Supplies.objects.all():
        product = item.product
        product.quantity += item.quantity
        product.save()
        supply = Journal.objects.create(
            type_of_operation = True,
            category = product.category,
            hero = product.hero,
            barcode = product.barcode,
            quantity = item.quantity,
            purchase = product.purchase
        )
        if product.barcode != "0000000000000":
            sum_of_operations += item.quantity * product.purchase

    Supplies.objects.all().delete()
    money = Products.objects.get(barcode="0000000000000")
    money.quantity -= sum_of_operations
    money.save()
    return redirect('journal:adding')


def sales_view(request):
    context = {
        'categories': Categories.objects.all(),
        'titles': Titles.objects.all(),
        'heroes': Heroes.objects.all(),
        'sales': Sales.objects.all(),
    }
    return render(request, 'journal/sales.html', context)


@csrf_exempt
def sales_confirm(request):
    data = json.loads(request.body.decode('utf-8'))
    cart_data = data.get('cart_data')

    for item in cart_data:
        item_id = item.get('itemId')
        cart_item = Sales.objects.get(id=item_id)
        cart_item.quantity = int(item.get('quantity'))
        cart_item.total_discount = int(item.get('discount'))
        cart_item.save()

    sum_of_operations = 0
    for item in Sales.objects.all():
        product = item.product
        product.quantity -= item.quantity
        product.save()
        
        sold = Journal.objects.create(
            type_of_operation = False,
            category = product.category,
            hero = product.hero,
            barcode = product.barcode,
            quantity = -item.quantity,
            price = product.price,
            total_discount = item.total_discount
        )
        if product.barcode != "0000000000000":
            sum_of_operations += item.quantity * product.price

    Sales.objects.all().delete()
    money = Products.objects.get(barcode="0000000000000")
    money.quantity += sum_of_operations
    money.save()
    return redirect('journal:sales')


@csrf_exempt
def remove_from_adding(request):
    item_id = request.POST.get('item_id')
    item = Supplies.objects.get(id=item_id)
    item.delete()
    return JsonResponse({'status': 'success'})


@csrf_exempt
def remove_from_sales(request):
    item_id = request.POST.get('item_id')
    item = Sales.objects.get(id=item_id)
    item.delete()
    return JsonResponse({'status': 'success'})
