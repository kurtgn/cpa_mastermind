# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastermind', '0004_auto_20151012_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='adverts',
            field=models.ManyToManyField(to='mastermind.Advert'),
        ),
    ]
