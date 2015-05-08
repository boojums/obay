# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('obay', '0014_auto_20150502_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(null=True, upload_to=b'item_images/'),
            preserve_default=True,
        ),
    ]
