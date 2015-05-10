# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obay', '0011_auto_20150501_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='is_active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
