from django.db import models
from common.utility import get_ulid
from item.models.item import ItemModel

class ReviewModel(models.Model):
    
    id = models.CharField(max_length=32, default=get_ulid, primary_key=True, editable=False)
   
    star = models.FloatField('レビューの★の数',null=True,default=0)
    title = models.CharField('レビュータイトル',max_length=100)
    content = models.TextField('レビュー内容',max_length=300)

    user_attr = models.CharField('属性',max_length=100,null=True)
    posted_at = models.DateField('',null=True)
    created_at = models.DateTimeField('作成日時',auto_now_add=True,null=True)
    updated_at = models.DateTimeField('更新日時',auto_now=True,null=True)

    item_id = models.ForeignKey(ItemModel,db_column="item_id",verbose_name='レビュー',on_delete=models.CASCADE,null=True,related_name='review')
    
    class Meta():
        db_table='review'