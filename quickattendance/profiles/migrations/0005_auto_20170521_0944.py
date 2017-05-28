# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 09:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='mentor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=25, null=True),
        ),
    ]