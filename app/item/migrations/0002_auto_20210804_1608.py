# Generated by Django 3.1.6 on 2021-08-04 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmodel',
            name='amazon_price',
            field=models.IntegerField(default=0, verbose_name='amazon最安値'),
        ),
        migrations.AddField(
            model_name='itemmodel',
            name='jan',
            field=models.IntegerField(default=0, null=True, verbose_name='JAN'),
        ),
        migrations.AddField(
            model_name='itemmodel',
            name='rakuten_price',
            field=models.IntegerField(default=0, verbose_name='rakuten最安値'),
        ),
        migrations.AddField(
            model_name='itemmodel',
            name='yahoo_price',
            field=models.IntegerField(default=0, verbose_name='yahoo最安値'),
        ),
        migrations.AddField(
            model_name='itemmodel',
            name='yahoo_review_count',
            field=models.IntegerField(default=0, null=True, verbose_name='レビュー数'),
        ),
        migrations.AddField(
            model_name='itemmodel',
            name='yahoo_star_average',
            field=models.FloatField(default=0, null=True, verbose_name='★の数の平均'),
        ),
    ]
