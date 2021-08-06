from django.urls import path
from .views.item_table import *  



app_name = 'item'
urlpatterns = [
    path('item-table', ItemTableView.as_view(), name="item-table"),

]
