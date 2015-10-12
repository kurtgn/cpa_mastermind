# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastermind', '0010_auto_20151012_1234'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Advert',
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name_plural': 'Адверты', 'verbose_name': 'Адверт'},
        ),
    ]
