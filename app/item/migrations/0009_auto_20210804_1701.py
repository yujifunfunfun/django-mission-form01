# Generated by Django 3.1.6 on 2021-08-04 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_auto_20210804_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時'),
        ),
    ]
