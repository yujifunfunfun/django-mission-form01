from django.db import models

from django.http import request
from django.utils import timezone
from common.utility import get_ulid

class ItemModel(models.Model):
    
    id = models.CharField(max_length=32, default=get_ulid, primary_key=True, editable=True)
    name = models.CharField('商品名', max_length=500, null=True)
    jan = models.CharField('JAN', max_length=64, null=True)
    description = models.TextField('説明文', null=True)

    price = models.IntegerField('価格', null=True, default=0)
    
    yahoo_price = models.IntegerField('yahoo最安値', null=True, default=0)
    yahoo_url = models.TextField('yahooURL',max_length=100,null=True,default='')
    rakuten_price = models.IntegerField('rakuten最安値', null=True, default=0)
    rakuten_url = models.TextField('rakutenURL',max_length=100,null=True,default='')
    amazon_price = models.IntegerField('amazon最安値', null=True, default=0)
    amazon_url = models.TextField('amazonURL',max_length=100,null=True,default='')
    yahoo_star_average = models.FloatField('★の数の平均',null=True,default=0)
    yahoo_review_count = models.IntegerField('レビュー数',null=True,default=0)

    thumbnail_url = models.TextField('サムネイルURL', null=True)
    created_at = models.DateTimeField('作成日時',auto_now_add=True,null=True)
    updated_at = models.DateTimeField('更新日時',auto_now=True,null=True)
    
    def __str__(self):
        return self.id
    
    def get_min_price(self):
        return min(self.yahoo_price,self.rakuten_price,self.amazon_price)
    
    def get_max_price(self):
        return max(self.yahoo_price,self.rakuten_price,self.amazon_price)
        
    class Meta():
        db_table='item'
        