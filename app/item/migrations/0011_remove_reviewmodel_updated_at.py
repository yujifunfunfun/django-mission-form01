# Generated by Django 3.1.6 on 2021-08-05 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0010_reviewmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewmodel',
            name='updated_at',
        ),
    ]
