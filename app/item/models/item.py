from django.db import models

from django.http import request
from django.utils import timezone
from common.utility import get_ulid

class ItemModel(models.Model):
    
    id = models.CharField(max_length=32, default=get_ulid, primary_key=True, editable=True)
    name = models.CharField('商品名', max_length=500, null=True)
    jan = models.CharField('JAN', max_length=64, null=True)
    description = models.TextField('説明文', null=True)    
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
    
    class Meta():
        db_table='item'
        
class User(models.Model):
    id = models.CharField(max_length=32, default=get_ulid, primary_key=True, editable=True)
    name = models.CharField('名前', max_length=500, null=True)
    favorite_item = models.ManyToManyField("ItemModel",null=True)

    class Meta():
        db_table='user'