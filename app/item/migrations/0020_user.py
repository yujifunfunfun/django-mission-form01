# Generated by Django 3.1.6 on 2021-08-08 21:15

import common.utility
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0019_auto_20210806_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(default=common.utility.get_ulid, max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500, null=True, verbose_name='名前')),
                ('favorite_item', models.ManyToManyField(to='item.ItemModel')),
            ],
        ),
    ]
