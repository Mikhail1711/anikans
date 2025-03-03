# Generated by Django 4.2.7 on 2024-11-14 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_remove_sales_barcode_remove_sales_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='hero',
            field=models.CharField(max_length=25, verbose_name='Персонаж'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='purchase',
            field=models.IntegerField(default=0, verbose_name='Закуп'),
        ),
    ]
