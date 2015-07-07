# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='language',
            field=models.CharField(default=b'en', max_length=100, blank=True, choices=[(b'en', 'English'), (b'es', 'Spanish')]),
        ),
    ]
