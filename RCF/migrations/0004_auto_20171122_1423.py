# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RCF', '0003_auto_20171122_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='InOut_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inout5_des', models.CharField(max_length=500)),
                ('inout5_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='InOut_6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inout6_des', models.CharField(max_length=500)),
                ('inout6_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='InOut_7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inout7_des', models.CharField(max_length=500)),
                ('inout7_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='InOut_8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inout8_des', models.CharField(max_length=500)),
                ('inout8_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.RenameModel(
            old_name='InOut_1_3',
            new_name='InOut_1',
        ),
        migrations.RenameModel(
            old_name='Inout_1_1',
            new_name='InOut_2',
        ),
        migrations.RenameModel(
            old_name='InOut_1_2',
            new_name='InOut_3',
        ),
        migrations.RenameModel(
            old_name='InOut_3_4',
            new_name='InOut_4',
        ),
        migrations.RenameField(
            model_name='inout_2',
            old_name='inout4_code',
            new_name='inout2_code',
        ),
        migrations.RenameField(
            model_name='inout_2',
            old_name='inout4_des',
            new_name='inout2_des',
        ),
        migrations.RenameField(
            model_name='inout_3',
            old_name='inout2_code',
            new_name='inout3_code',
        ),
        migrations.RenameField(
            model_name='inout_3',
            old_name='inout2_des',
            new_name='inout3_des',
        ),
        migrations.RenameField(
            model_name='inout_4',
            old_name='inout3_code',
            new_name='inout4_code',
        ),
        migrations.RenameField(
            model_name='inout_4',
            old_name='inout3_des',
            new_name='inout4_des',
        ),
    ]
