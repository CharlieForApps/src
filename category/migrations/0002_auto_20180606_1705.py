# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-06 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cattype',
            field=models.CharField(help_text='Input Expense / Income.', max_length=120),
        ),
    ]
