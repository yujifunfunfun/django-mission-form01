from django.urls import path
from .views.item_register import *  
from .views.item_table import *  



app_name = 'item'
urlpatterns = [
    path('register', ItemRegisterView.as_view(), name="register"),
    path('item-table', ItemTableView.as_view(), name="item-table"),

]
