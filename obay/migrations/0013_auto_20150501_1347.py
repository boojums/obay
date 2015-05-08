# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('obay', '0012_auction_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='auction',
            field=models.ForeignKey(to='obay.Auction'),
        ),
        migrations.AlterField(
            model_name='item',
            name='donor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
