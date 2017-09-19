# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 06:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrooge', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cost',
            options={'ordering': ('-predicted_cost',)},
        ),
        migrations.RemoveField(
            model_name='cost',
            name='allocated_percentage',
        ),
        migrations.AddField(
            model_name='costbreakdown',
            name='finyear_percentage',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='costbreakdown',
            name='predicted_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
