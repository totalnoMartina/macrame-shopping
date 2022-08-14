from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shoppingcart, name='view_cart'),
    path('add/<item_id>/', views.add_to_shoppingcart, name='add_to_cart'),
    path('adjust/<tem_id>/', views.adjust_shoppingcart, name='adjust_cart'),
    path('remove/<item_id>/', views.remove_from_shoppingcart, name='remove_from_cart'),

]