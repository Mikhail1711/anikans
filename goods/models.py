from django.core.validators import RegexValidator
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='Название')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Titles(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name='Название')
    game = models.BooleanField(verbose_name='Игра')

    class Meta:
        db_table = 'titles'
        verbose_name = 'Тайтл'
        verbose_name_plural = 'Тайтлы'

    def __str__(self):
        return self.name

class Heroes(models.Model):
    title = models.ForeignKey(to=Titles, on_delete=models.PROTECT, verbose_name='Тайтл')
    name = models.CharField(max_length=25, unique=True, verbose_name='Имя',)
    
    class Meta:
        db_table = 'heroes'
        verbose_name = 'Персонажа'
        verbose_name_plural = 'Персонажи'

    def __str__(self):
        return f'{self.name} -- {self.title.name}'


class Products(models.Model):
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Категория')
    hero = models.ForeignKey(to=Heroes, on_delete=models.PROTECT, verbose_name='Персонаж')

    digits_only = RegexValidator(r'^\d{13}$', 'Введите 13 цифр')
    barcode = models.CharField(max_length=13, unique=True, validators=[digits_only], verbose_name='Штрих-код')
    item = models.CharField(max_length=13, blank=True, verbose_name='Артикул')
    description = models.TextField(max_length=100, blank=True, verbose_name='Описание')
    purchase = models.IntegerField(null=False, verbose_name='Закуп')
    price = models.IntegerField(null=False, verbose_name='Цена')
    quantity = models.IntegerField(null=False, verbose_name='Кол-во')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ("id",)
    
    def __str__(self):
        return f'{self.category.name} ШК {self.barcode[-6:]} остаток {self.quantity} шт.'
    
    def readable_barcode(self):
        return f'{self.barcode[0]} {self.barcode[1:-6]} {self.barcode[-6:]}'

    def save(self, *args, **kwargs):
        # Переопределение save() родительского класса для учета закупа новых товаров
        super().save(*args, **kwargs)

        if self.pk is None and self.barcode != "0000000000000":
            money = Products.objects.get(barcode="0000000000000")
            money.quantity -= self.purchase * self.quantity
            money.save()
            from journal.models import Journal

            created = Journal.objects.create(
                type_of_operation = True,
                category = self.category,
                hero = self.hero,
                barcode = self.barcode,
                quantity = self.quantity,
                purchase = self.purchase
                )
