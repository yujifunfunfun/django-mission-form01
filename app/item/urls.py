from django.urls import path,include
from .views.item_table import *  
from .views.auth0 import *
from .views.favorite import *

app_name = 'item'
urlpatterns = [
    path('item-table', ItemTableView.as_view(), name="item-table"),
    path('favorite/<pk>/', Favorite.as_view(), name="favorite"),
    path('', index),
    path('dashboard', dashboard,name='dashboard'),
    path('logout', logout),

]
