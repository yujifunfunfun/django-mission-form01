from django.db import models
from django.views import generic
from django.shortcuts import render,redirect
from django.views.generic import View
from ..models.item import *
from ..tables.item import *
from django.contrib.auth.mixins import LoginRequiredMixin

# お気に入り追加
class AddFavorite(LoginRequiredMixin,View):
    def get(self,request,pk):
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)
        item = ItemModel.objects.get(id=pk)
        user.favorite_item.add(item)

        return redirect('item:item-table')


# お気に入り削除
class DeleteFavorite(LoginRequiredMixin,View):
    def get(self,request,pk):
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)
        user.favorite_item.remove(ItemModel.objects.get(id=pk))
        return redirect('item:favorite-item')


# お気に入り商品一覧テーブル
class FavoriteTableView(LoginRequiredMixin,generic.TemplateView):
    template_name = "item/favorite-item.html"

    def get(self, request, *args, **kwargs):
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)
        fav_items = user.favorite_item.all()
        table = FavoriteTable(fav_items)
        table.paginate(page=request.GET.get("page", 1), per_page=25)
        user_id = self.request.user.id
        if not User.objects.filter(pk=user_id).exists():
            user = User.objects.create(id=user_id)
            user.save()

        return self.render_to_response({'table': table, 'count': fav_items.count()})