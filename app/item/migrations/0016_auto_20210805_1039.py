# Generated by Django 3.1.6 on 2021-08-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0015_auto_20210805_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='user_attr',
            field=models.CharField(max_length=100, null=True, verbose_name='属性'),
        ),
    ]