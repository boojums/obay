# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obay', '0008_auto_20150428_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='team',
            new_name='isteam',
        ),
    ]
