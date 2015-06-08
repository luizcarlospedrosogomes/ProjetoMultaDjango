# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controleUsuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name_plural': 'usuarios', 'verbose_name': 'usuario', 'ordering': ['nome']},
        ),
    ]
