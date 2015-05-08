# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obay', '0018_auto_20150507_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='donor',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
