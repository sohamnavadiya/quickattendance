# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20170513_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sabhasession',
            name='status',
            field=models.CharField(choices=[(b'active', b'active'), (b'close', b'close'), (b'pending', b'pending'), (b'removed', b'removed')], default=b'active', max_length=20),
        ),
    ]
