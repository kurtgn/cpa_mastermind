# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastermind', '0012_auto_20151012_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='forum_name',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='skype_name',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
    ]
