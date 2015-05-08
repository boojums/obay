# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obay', '0003_auto_20150428_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='slug',
        ),
    ]
