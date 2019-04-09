# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-03 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0064_auto_20190329_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='primarypage',
            name='intro_de',
            field=models.CharField(blank=True, help_text='Intro paragraph to show in hero cutout box', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='primarypage',
            name='intro_en',
            field=models.CharField(blank=True, help_text='Intro paragraph to show in hero cutout box', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='primarypage',
            name='intro_es',
            field=models.CharField(blank=True, help_text='Intro paragraph to show in hero cutout box', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='primarypage',
            name='intro_fr',
            field=models.CharField(blank=True, help_text='Intro paragraph to show in hero cutout box', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='primarypage',
            name='intro_pl',
            field=models.CharField(blank=True, help_text='Intro paragraph to show in hero cutout box', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='primarypage',
            name='intro_pt',
            field=models.CharField(blank=True, help_text='Intro paragraph to show in hero cutout box', max_length=250, null=True),
        ),
    ]