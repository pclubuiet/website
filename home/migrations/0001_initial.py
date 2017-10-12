# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('language', models.CharField(max_length=30)),
                ('example', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Resource')),
            ],
            options={
                'ordering': ('headline',),
            },
        ),
    ]
