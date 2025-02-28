from django.contrib import admin

from goods.models import Categories, Titles, Heroes, Products
from journal.models import Journal


class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']


class TitlesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']


class HeroesAdmin(admin.ModelAdmin):#
    autocomplete_fields = ['title']
    search_fields = ['name', 'title__name']
    list_display = ['name', 'title']
    list_filter = ['title']
    ordering = ['title', 'name']


class ProductsAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category', 'hero']
    list_display = ['category_name', 'title_name', 'hero_name', 'displayed_barcode', 'displayed_item', 'purchase', 'price', 'quantity']
    list_filter = ['category', 'hero__title']
    ordering = ['id']

    def save_model(self, request, obj, form, change):
        

        if obj.pk is None and obj.barcode != "0000000000000":
            money = Products.objects.get(barcode="0000000000000")
            money.quantity -= obj.purchase * obj.quantity
            money.save()
            from journal.models import Journal
            created = Journal.objects.create(
                type_of_operation = True,
                category = obj.category,
                hero = obj.hero,
                barcode = obj.barcode,
                quantity = obj.quantity,
                purchase = obj.purchase
                )
        super().save_model(request, obj, form, change)

    def category_name(self, obj):
        return obj.category.name
    
    category_name.short_description = 'Категория'

    def title_name(self, obj):
        return f'{obj.hero.title.name:.10}'
    
    title_name.short_description = 'Тайтл'

    def hero_name(self, obj):
        return f'{obj.hero.name:.10}'
    
    hero_name.short_description = 'Персонаж'

    def displayed_barcode(self, obj):
        return f'...{obj.barcode[-6:]}'
    
    displayed_barcode.short_description = 'Штрих-код'

    def displayed_item(self, obj):
        return f'...{obj.item[-7:]}'
    
    displayed_item.short_description = 'Артикул'



admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Titles, TitlesAdmin)
admin.site.register(Heroes, HeroesAdmin)#
admin.site.register(Products, ProductsAdmin)
