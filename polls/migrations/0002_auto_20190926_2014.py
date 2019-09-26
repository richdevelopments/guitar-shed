# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-26 20:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='number_of_votes',
        ),
        migrations.AddField(
            model_name='option',
            name='voters',
            field=models.ManyToManyField(related_name='voters', to=settings.AUTH_USER_MODEL),
        ),
    ]
