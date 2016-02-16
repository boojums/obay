# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('obay', '0020_auto_20150508_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='item',
            name='pic',
            field=django_resized.forms.ResizedImageField(null=True, upload_to=b'item_images/'),
        ),
    ]
