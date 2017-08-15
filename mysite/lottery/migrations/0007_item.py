# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-21 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0006_moneylostone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('data', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
