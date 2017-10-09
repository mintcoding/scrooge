# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrooge', '0005_itsystem_user_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergroup',
            name='cost_data',
        ),
        migrations.AddField(
            model_name='usergroup',
            name='predicted_cost',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=12),
        ),
    ]