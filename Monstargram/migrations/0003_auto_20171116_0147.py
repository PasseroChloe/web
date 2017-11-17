# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monstargram', '0002_auto_20171115_0633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resource',
            options={'verbose_name': '资源', 'verbose_name_plural': '资源'},
        ),
        migrations.AlterModelOptions(
            name='usercomment',
            options={'verbose_name': '用户评论', 'verbose_name_plural': '用户评论'},
        ),
        migrations.AlterModelOptions(
            name='userlikes',
            options={'verbose_name': '用户点赞', 'verbose_name_plural': '用户点赞'},
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(editable=False, max_length=64),
        ),
    ]
