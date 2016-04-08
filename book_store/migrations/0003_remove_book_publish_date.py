# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0002_book_publish_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publish_date',
        ),
    ]
