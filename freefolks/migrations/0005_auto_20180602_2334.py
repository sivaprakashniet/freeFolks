# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freefolks', '0004_auto_20180602_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='bank_name',
            field=models.CharField(max_length=50, verbose_name=b'Select your bank'),
        ),
    ]