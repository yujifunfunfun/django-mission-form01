# Generated by Django 3.1.6 on 2021-08-23 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0024_auto_20210809_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorite_item',
            field=models.ManyToManyField(null=True, to='item.ItemModel'),
        ),
    ]