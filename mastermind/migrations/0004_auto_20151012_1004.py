# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastermind', '0003_auto_20151012_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='AffiliateNetwork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='affiliate_networks',
            field=models.ManyToManyField(to='mastermind.AffiliateNetwork'),
        ),
        migrations.AddField(
            model_name='post',
            name='offers',
            field=models.ManyToManyField(to='mastermind.Offer'),
        ),
    ]
