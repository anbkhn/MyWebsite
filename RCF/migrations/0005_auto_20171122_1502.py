# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RCF', '0004_auto_20171122_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='inout_1',
            name='inout1_config',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inout_2',
            name='inout2_config',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inout_3',
            name='inout3_config',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inout_4',
            name='inout4_config',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inout_5',
            name='inout5_config',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inout_6',
            name='inout6_config',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inout_7',
            name='inout7_config',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inout_8',
            name='inout8_config',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
