# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0005_requests'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Requests',
            new_name='RequestRecord',
        ),
    ]
