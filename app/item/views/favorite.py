from django.db import models
from django.views import generic
from django.shortcuts import render,redirect
from django.views.generic import View
from ..models.item import *
from django.contrib.auth.mixins import LoginRequiredMixin


class Favorite(LoginRequiredMixin,View):
    def get(self,request,pk):
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)
        item = ItemModel.objects.get(id=pk)
        user.favorite_item.add(item)

        return redirect('item:item-table')