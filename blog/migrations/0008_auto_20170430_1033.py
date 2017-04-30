# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 02:33
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170428_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cover_caption',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, upload_to=blog.models.post_cover_path),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'published'), (2, 'draft'), (3, 'hidden')], default=1),
            preserve_default=False,
        ),
    ]
