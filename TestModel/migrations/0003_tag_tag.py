# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-09 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_contact_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='tag',
            field=models.CharField(default=b'default', max_length=50),
        ),
    ]
