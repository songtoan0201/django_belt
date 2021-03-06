# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-15 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20191114_1356'),
        ('trip_buddy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='joined_by',
            field=models.ManyToManyField(related_name='join', to='login.User'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_trips', to='login.User'),
        ),
    ]
