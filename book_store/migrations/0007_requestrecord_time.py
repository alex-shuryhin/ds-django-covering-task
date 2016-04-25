# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0006_auto_20160407_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestrecord',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
