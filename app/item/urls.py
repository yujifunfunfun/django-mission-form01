from django.urls import path,include
from .views.item_table import *  
from .views.auth0 import *
from .views.favorite import *

app_name = 'item'
urlpatterns = [
    path('item-table', ItemTableView.as_view(), name="item-table"),
    path('favorite/<pk>/', AddFavorite.as_view(), name="favorite"),
    path('delete-favorite/<pk>/', DeleteFavorite.as_view(), name="delete-favorite"),
    path('favorite-item', FavoriteTableView.as_view(), name="favorite-item"),
    path('', index),
    path('dashboard', dashboard,name='dashboard'),
    path('logout', logout),

]
