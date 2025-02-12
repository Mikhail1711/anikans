# Generated by Django 4.2.7 on 2024-11-01 08:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Heroes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Персонажа',
                'verbose_name_plural': 'Персонажи',
                'db_table': 'heroes',
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='Название')),
                ('game', models.BooleanField(verbose_name='Игра')),
            ],
            options={
                'verbose_name': 'Тайтл',
                'verbose_name_plural': 'Тайтлы',
                'db_table': 'titles',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator('^\\d{13}$', 'Введите 13 цифр')], verbose_name='Штрих-код')),
                ('item', models.CharField(blank=True, max_length=13, verbose_name='Артикул')),
                ('description', models.TextField(blank=True, max_length=100, verbose_name='Описание')),
                ('purchase', models.IntegerField(verbose_name='Закуп')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('quantity', models.IntegerField(verbose_name='Кол-во')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goods.categories', verbose_name='Категория')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goods.heroes', verbose_name='Персонаж')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goods.titles', verbose_name='Тайтл')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'product',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='heroes',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goods.titles', verbose_name='Тайтл'),
        ),
    ]
