# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recoup', '0002_remove_bill_allocated'),
    ]

    operations = [
        migrations.AddField(
            model_name='itsystem',
            name='cost_centre',
            field=models.CharField(default='N/A', max_length=24),
            preserve_default=False,
        ),
    ]
