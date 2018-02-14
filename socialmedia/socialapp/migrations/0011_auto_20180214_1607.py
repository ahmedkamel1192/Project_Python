# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0010_auto_20180214_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='post_id',
            field=models.ForeignKey(to='socialapp.Comment'),
        ),
    ]
