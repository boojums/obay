# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('obay', '0013_auto_20150501_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pic',
            field=django_resized.forms.ResizedImageField(upload_to=b'item_images/'),
        ),
    ]
