from django.views import generic
from ..models.item import *
from ..tables.item import *
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


class ItemTableView(generic.TemplateView):
    template_name = "item/item-table.html"

    def get(self, request, *args, **kwargs):
        items = ItemModel.objects.all()
        table = ItemTable(items)
        table.paginate(page=request.GET.get("page", 1), per_page=25)
        user_id = self.request.user.id
        if not User.objects.filter(pk=user_id).exists():
            user = User.objects.create(id=user_id)
            user.save()

        return self.render_to_response({'table': table, 'count': items.count()})

    def post(self, request, *args, **kwargs):
        item_obj = ItemModel.objects.all()

        # 検索キーワード指定
        keyword = self.request.POST['keyword']
        if keyword:
            item_obj = item_obj.filter(Q(name__contains=keyword) | Q(jan__contains=keyword))

        # 詳細検索条件指定
        min_price = self.request.POST['min_price']
        max_price = self.request.POST['max_price']
        if min_price:
            item_obj = item_obj.filter(yahoo_price__gte=min_price)
        if max_price:
            item_obj = item_obj.filter(yahoo_price__lte=max_price)
        
        min_review_count = self.request.POST['min_review_count']
        if min_review_count:
            item_obj = item_obj.filter(yahoo_review_count__gte=min_review_count)
            
        min_star_count = self.request.POST['min_star_count']
        if min_star_count:
            item_obj = item_obj.filter(yahoo_star_average__gte=min_star_count)

        table = ItemTable(item_obj)
        table.paginate(page=request.POST.get("page", 1), per_page=25)
        
        return self.render_to_response({'table': table, 'count': item_obj.count()})


