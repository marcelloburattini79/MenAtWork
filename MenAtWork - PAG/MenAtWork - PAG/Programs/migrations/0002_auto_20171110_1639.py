# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-10 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Programs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='ragioneSociale',
            new_name='RagioneSociale',
        ),
        migrations.AddField(
            model_name='cliente',
            name='CAPComune',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Cap e Comune'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='CAPFat',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='CAP fatturazione'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Comune',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Comune'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Email',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Email2',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Email3',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Email1'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Fax',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='FAX'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Fax2',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Fax'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Fax3',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Fax1'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Indirizzo',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Indirizzo'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Intestazione',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Intestazione'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='PartitaIva',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Partita Iva'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='RSComune',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Ragione Sociale e Comune'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Referente2',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Referente'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Referente3',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Referente'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Telefono',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Telefono'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Telefono2',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Telefono'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Telefono3',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Telefono1'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='codiceCliente',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Codice cliente'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='codiceFiscale',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Codice Fiscale'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cognome2',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Cognome'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cognome3',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Cognome'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='comuneFat',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Comune fatturazione'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='condizioniPagamento',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Condizioni di pagamento'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='indirizzoFat',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Indirizzo fatturazione'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='note',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Note'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='titolo2',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Titolo'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='titolo3',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Titolo'),
        ),
        migrations.AlterField(
            model_name='task',
            name='personaleAssente',
            field=models.ManyToManyField(blank=True, related_name='assenze', to='Programs.Tecnico', verbose_name='Presonale assente'),
        ),
    ]