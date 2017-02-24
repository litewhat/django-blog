# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('articles', '0005_auto_20170224_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile'),
            preserve_default=False,
        ),
    ]