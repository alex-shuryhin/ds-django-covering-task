# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 7, 9, 40, 52, 315654, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
