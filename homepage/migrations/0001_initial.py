# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-19 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dpotw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
            ],
            options={
                'verbose_name': 'Django Package of the Week',
                'verbose_name_plural': 'Django Packages of the Week',
                'ordering': ('-start_date', '-end_date'),
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Gotw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('grid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grid.Grid')),
            ],
            options={
                'verbose_name': 'Grid of the Week',
                'verbose_name_plural': 'Grids of the Week',
                'ordering': ('-start_date', '-end_date'),
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='PSA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('body_text', models.TextField(blank=True, null=True, verbose_name='PSA Body Text')),
            ],
            options={
                'verbose_name': 'Public Service Announcement',
                'verbose_name_plural': 'Public Service Announcements',
                'ordering': ('-created',),
                'get_latest_by': 'created',
            },
        ),
    ]