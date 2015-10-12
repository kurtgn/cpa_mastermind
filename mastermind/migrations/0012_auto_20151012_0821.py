# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastermind', '0011_auto_20151012_0741'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adnetwork',
            options={'verbose_name_plural': 'Источники трафика', 'verbose_name': 'Источник трафика'},
        ),
        migrations.AlterModelOptions(
            name='affiliatenetwork',
            options={'verbose_name_plural': 'Офферные сети', 'verbose_name': 'Сеть'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Гео', 'verbose_name': 'Гео'},
        ),
        migrations.AlterModelOptions(
            name='offer',
            options={'verbose_name_plural': 'Офферы', 'verbose_name': 'Оффер'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Посты', 'verbose_name': 'Пост'},
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='post',
            name='details',
            field=models.TextField(max_length=500, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(unique=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(verbose_name='Адверт', to='mastermind.CustomUser'),
        ),
    ]
