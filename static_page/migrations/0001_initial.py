# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-12-13 16:36
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Corpo')),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
    ]
