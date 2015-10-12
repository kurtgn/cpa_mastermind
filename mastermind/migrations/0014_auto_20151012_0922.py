# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastermind', '0013_auto_20151012_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adnetwork',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='affiliatenetwork',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='forum_name',
            field=models.CharField(null=True, max_length=50, blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
