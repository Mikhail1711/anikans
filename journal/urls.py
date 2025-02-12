from django.urls import path

from journal import views

app_name = 'journal'

urlpatterns = [
    path('history/', views.history_view, name='history'),
    
    path('adding/', views.adding_view, name='adding'),
    path('adding-remove/', views.remove_from_adding, name='remove_from_adding'),
    path('adding-confirm/', views.adding_confirm, name='adding_confirm'),

    path('sales/', views.sales_view, name='sales'),
    path('sales-remove/', views.remove_from_sales, name='remove_from_sales'),
    path('sales-confirm/', views.sales_confirm, name='sales_confirm'),
]
