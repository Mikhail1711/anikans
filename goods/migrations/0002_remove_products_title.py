# Generated by Django 4.2.7 on 2024-11-13 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='title',
        ),
    ]
