from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_to_list/', views.add_to_list, name='add_to_list'),
]
