# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-06 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher_num',
            field=models.IntegerField(default=0),
        ),
    ]
