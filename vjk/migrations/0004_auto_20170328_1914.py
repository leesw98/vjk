# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 02:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vjk', '0003_auto_20170328_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsors',
            name='primary_contact',
        ),
        migrations.RemoveField(
            model_name='sponsors',
            name='secondary_contact',
        ),
    ]
