# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160718191935 on 2016-08-30 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_auto_20160829_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dept_id',
            field=models.IntegerField(max_length=10, primary_key=True, serialize=False),
        ),
    ]