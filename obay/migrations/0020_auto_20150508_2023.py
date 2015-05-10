# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obay', '0019_item_donor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='donor',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
