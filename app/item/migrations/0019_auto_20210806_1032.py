# Generated by Django 3.1.6 on 2021-08-06 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0018_auto_20210805_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemmodel',
            name='price',
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='item_id',
            field=models.ForeignKey(db_column='item_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='item.itemmodel', verbose_name='レビュー'),
        ),
    ]