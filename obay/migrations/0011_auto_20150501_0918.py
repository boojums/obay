# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('obay', '0010_bid_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='item',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='auction',
            field=models.ForeignKey(to='obay.Auction', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='donor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='pic',
            field=models.ImageField(upload_to=b'item_images/'),
        ),
    ]
