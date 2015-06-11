# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controleUsuario', '0002_auto_20150604_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('gravidade', models.IntegerField(max_length=10)),
                ('local', models.CharField(max_length=200)),
                ('numeros_de_pontos', models.IntegerField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={},
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
    ]
