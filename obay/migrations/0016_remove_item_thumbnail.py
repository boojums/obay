# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obay', '0015_item_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='thumbnail',
        ),
    ]
