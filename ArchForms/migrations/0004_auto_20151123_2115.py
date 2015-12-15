# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArchForms', '0003_auto_20151121_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklyreport',
            name='week_number',
            field=models.IntegerField(default=48),
        ),
    ]
