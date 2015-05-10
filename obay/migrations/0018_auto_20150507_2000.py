# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obay', '0017_auction_bidding_open'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='donor',
            new_name='contact',
        ),
    ]
