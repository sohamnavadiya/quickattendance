# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20170531_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='karyakar_type',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.UserType'),
        ),
    ]