# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastermind', '0005_post_adverts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='adverts',
        ),
        migrations.AddField(
            model_name='post',
            name='advert',
            field=models.ForeignKey(default=1, to='mastermind.Advert'),
            preserve_default=False,
        ),
    ]
