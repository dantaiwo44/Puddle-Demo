from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.browse, name='browse'),
    path('new/', views.new_item, name='new_item'),
    path('<int:primary_key>/', views.detail, name='item_detail'),
    path('<int:primary_key>/delete/', views.delete, name='delete_item'),
]