# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-12 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('email', models.CharField(default='', max_length=254)),
                ('subject', models.CharField(default='', max_length=254)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
