from django.contrib import admin
from .models.item import ItemModel
from .models.review import ReviewModel


admin.site.register(ItemModel)
admin.site.register(ReviewModel)