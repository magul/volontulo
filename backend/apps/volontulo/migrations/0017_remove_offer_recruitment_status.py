# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-22 19:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volontulo', '0016_remove_offer_status_old'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='recruitment_status',
        ),
    ]