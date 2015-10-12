# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastermind', '0008_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='advert',
        ),
        migrations.AddField(
            model_name='customuser',
            name='forum_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to='mastermind.CustomUser', default=1),
            preserve_default=False,
        ),
    ]
