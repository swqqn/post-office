# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-30 08:54
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('post_office', '0007_auto_20170731_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='headers',
            field=jsonfield.fields.JSONField(blank=True, null=True, verbose_name='Headers'),
        ),
    ]
