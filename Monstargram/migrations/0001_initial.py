# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 06:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_title', models.CharField(max_length=160)),
                ('resource_url', models.CharField(max_length=1200)),
                ('resource_image', models.ImageField(null=True, upload_to='')),
                ('upload_time', models.DateTimeField(verbose_name='date the resource uploaded')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=60, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=600)),
                ('comment_time', models.DateTimeField(verbose_name='date when the user made this comment')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monstargram.User')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Monstargram.Resource')),
            ],
        ),
        migrations.CreateModel(
            name='UserLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(verbose_name='date when the user click at this')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='Monstargram.Resource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monstargram.User')),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monstargram.User'),
        ),
    ]
