# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-23 01:33
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_auto_20180423_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adimage',
            name='image',
            field=filer.fields.image.FilerImageField(max_length=255, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='filer.Image', verbose_name='Image'),
        ),
    ]
