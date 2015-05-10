# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obay', '0016_remove_item_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='bidding_open',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
