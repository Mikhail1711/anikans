# Generated by Django 4.2.7 on 2024-11-14 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_alter_journal_hero_alter_journal_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Кол-во'),
        ),
        migrations.AlterField(
            model_name='supplies',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Кол-во'),
        ),
    ]
