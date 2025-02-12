from django.db import models


class Journal(models.Model):
    type_of_operation = models.BooleanField(verbose_name='INCOME')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    category = models.CharField(max_length=20, verbose_name='Категория')
    hero = models.CharField(max_length=25, verbose_name='Персонаж')
    barcode = models.CharField(max_length=13, verbose_name='Штрих-код')
    quantity = models.IntegerField(null=False,  verbose_name='Кол-во')
    purchase = models.IntegerField(default=0,  verbose_name='Закуп')
    price = models.IntegerField(default=0,  verbose_name='Цена')
    total_discount = models.IntegerField(default=0, verbose_name='Суммарная скидка')

    class Meta:
        db_table = 'journal'
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'
        ordering = ("-id",)
    
    def __str__(self):
        if self.type_of_operation:
            type = 'Закупка'
        else:
            type = 'Продажа'
        return f'{type} {self.category} - {self.quantity} шт. ШК {self.barcode[-6:]}'
    
    def type_display(self):
        if self.type_of_operation:
            type_d = 'ЗАКУПКА'
        else:
            type_d = 'ПРОДАЖА'
        return type_d
    
    def readable_barcode(self):
        return f'{self.barcode[0]} {self.barcode[1:-6]} {self.barcode[-6:]}'
    
    def total_sum(self):
        if self.type_of_operation:
            return (-1) * self.purchase * self.quantity
        else:
            return (-1) * self.price * self.quantity - self.total_discount
    
    def calcucations_display(self):
        if self.type_of_operation:
            return f'{self.quantity} шт. × {self.purchase} ₽'
        else:
            return f'{self.quantity} шт. × {self.price} ₽ — {self.total_discount} скидка'


class Supplies(models.Model):
    from goods import models as goods

    product = models.ForeignKey(to=goods.Products, on_delete=models.CASCADE, null=True, verbose_name='Товар')
    quantity = models.IntegerField(default=0, verbose_name='Кол-во')

    class Meta:
        db_table = 'supplies'
        verbose_name = 'Закупка'
        verbose_name_plural = 'Закупки'
        ordering = ("id",)
    
    def __str__(self):
        return f'Закупка {self.product.category} ШК ...{self.product.barcode[-6:]} - {self.quantity} шт.'
    
    def total_sum(self):
        return self.product.purchase * self.quantity


class Sales(models.Model):
    from goods import models as goods

    product = models.ForeignKey(to=goods.Products, on_delete=models.CASCADE, null=True, verbose_name='Товар')
    quantity = models.IntegerField(default=0, verbose_name='Кол-во')
    total_discount = models.IntegerField(default=0, verbose_name='Суммарная скидка')

    class Meta:
        db_table = 'sales'
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'
        ordering = ("id",)
    
    def __str__(self):
        discount = ''
        if self.total_discount:
            discount = f'Скидка {self.total_discount}р'
        return f'Продажа {self.product.category} ШК ...{self.product.barcode[-6:]} - {self.quantity} шт. {discount}'
    
    def total_price(self):
        return self.product.price * self.quantity - self.total_discount
