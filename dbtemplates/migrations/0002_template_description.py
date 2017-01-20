# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-20 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbtemplates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='description',
            field=models.CharField(default='Untitled template', help_text='Model instance text shown in admin area', max_length=100, verbose_name='Template description'),
            preserve_default=False,
        ),
    ]
