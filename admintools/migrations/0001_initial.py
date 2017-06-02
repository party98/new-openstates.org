# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-02 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataQualityIssues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('alert', models.CharField(choices=[('error', 'Error'), ('warning', 'Warning')], max_length=50)),
                ('issue', models.CharField(choices=[('address', 'Missing Postal Address'), ('email', 'Missing Email'), ('voice', 'Missing Voice Phone'), ('image', 'Missing Image URL')], max_length=50)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dataquality_issues', to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'opencivicdata_dataqualityissues',
            },
        ),
        migrations.AlterIndexTogether(
            name='dataqualityissues',
            index_together=set([('alert', 'issue')]),
        ),
    ]
