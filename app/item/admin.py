from django.contrib import admin
from .models.item import *
from .models.review import ReviewModel


admin.site.register(ItemModel)
admin.site.register(ReviewModel)
admin.site.register(User)
