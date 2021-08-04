# Generated by Django 3.1.6 on 2021-08-05 05:43

import common.utility
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_auto_20210804_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.CharField(default=common.utility.get_ulid, editable=False, max_length=32, primary_key=True, serialize=False)),
                ('star', models.FloatField(default=0, null=True, verbose_name='レビューの★の数')),
                ('title', models.CharField(max_length=100, verbose_name='レビュータイトル')),
                ('content', models.TextField(max_length=300, verbose_name='レビュー内容')),
                ('user_attr', models.CharField(max_length=100, verbose_name='属性')),
                ('posted_at', models.DateField(null=True, verbose_name='')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.itemmodel')),
            ],
            options={
                'db_table': 'review',
            },
        ),
    ]
