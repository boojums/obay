# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('obay', '0021_auto_20150511_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pic',
            field=django_resized.forms.ResizedImageField(upload_to=b'item_images/'),
        ),
    ]
