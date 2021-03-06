# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-04 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20180904_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentrecord',
            name='status',
            field=models.IntegerField(choices=[(1, '未审核'), (2, '已审核')], default=1, verbose_name='审核'),
        ),
        migrations.AlterField(
            model_name='studyrecord',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='提交作业日期'),
        ),
    ]
