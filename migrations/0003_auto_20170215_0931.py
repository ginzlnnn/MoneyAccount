# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 09:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20170215_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='revenue_text',
            new_name='income_text',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='pub_date',
            new_name='save_date',
        ),
    ]