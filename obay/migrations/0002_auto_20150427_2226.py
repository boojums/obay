# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obay', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
        migrations.RemoveField(
            model_name='bids',
            name='item',
        ),
        migrations.DeleteModel(
            name='Bids',
        ),
        migrations.AddField(
            model_name='bid',
            name='item',
            field=models.ForeignKey(to='obay.Item'),
            preserve_default=True,
        ),
    ]
