# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0016_auto_20180214_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='c_body',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='posts',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='posts',
            name='img',
            field=models.ImageField(upload_to=b'static/img/', blank=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='posts',
            name='p_body',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='posts',
            name='tag',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='reply',
            name='R_body',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='reply',
            name='post_id',
            field=models.ForeignKey(to='socialapp.Comment'),
        ),
        migrations.AlterField(
            model_name='unwanted',
            name='word',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]