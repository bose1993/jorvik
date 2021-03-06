# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-10-28 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0048_auto_20180917_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delega',
            name='tipo',
            field=models.CharField(choices=[('PR', 'Presidente'), ('CM', 'Commissario'), ('US', 'Ufficio Soci'), ('UU', 'Ufficio Soci Unità territoriali'), ('DA', "Delegato d'Area"), ('O1', 'Delegato Obiettivo I (Salute)'), ('O2', 'Delegato Obiettivo II (Sociale)'), ('O3', 'Delegato Obiettivo III (Emergenze)'), ('O4', 'Delegato Obiettivo IV (Principi)'), ('O5', 'Delegato Obiettivo V (Giovani)'), ('O6', 'Delegato Obiettivo VI (Sviluppo)'), ('RA', "Responsabile d'Area"), ('RE', 'Referente Attività'), ('GR', 'Referente Gruppo'), ('CO', 'Delegato Centrale Operativa'), ('RF', 'Responsabile Formazione'), ('DC', 'Direttore Corso'), ('AP', 'Responsabile Autoparco')], db_index=True, max_length=2),
        ),
    ]
