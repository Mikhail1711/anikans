from django.contrib import admin

from goods.models import Categories, Titles, Heroes, Products


class Heroesdmin(admin.ModelAdmin):
    list_display = ['name', 'title']
    list_filter = ['title']
    ordering = ['title']


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'title_name', 'hero_name', 'displayed_barcode', 'displayed_item', 'purchase', 'price', 'quantity']
    list_filter = ['category', 'hero__title']
    ordering = ['id']

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



admin.site.register(Categories)
admin.site.register(Titles)
admin.site.register(Heroes, Heroesdmin)
admin.site.register(Products, ProductsAdmin)
