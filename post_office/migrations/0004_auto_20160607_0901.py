# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 07:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import post_office.models


class Migration(migrations.Migration):

    dependencies = [
        ('post_office', '0003_longer_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'verbose_name': 'Attachment', 'verbose_name_plural': 'Attachments'},
        ),
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name': 'Email', 'verbose_name_plural': 'Emails'},
        ),
        migrations.AlterModelOptions(
            name='log',
            options={'verbose_name': 'Log', 'verbose_name_plural': 'Logs'},
        ),
        migrations.AlterField(
            model_name='attachment',
            name='emails',
            field=models.ManyToManyField(related_name='attachments', to='post_office.Email', verbose_name='Email addresses'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to=post_office.models.get_upload_path, verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='name',
            field=models.CharField(help_text='The original filename', max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='email',
            name='backend_alias',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Backend alias'),
        ),
        migrations.AlterField(
            model_name='email',
            name='context',
            field=jsonfield.fields.JSONField(blank=True, null=True, verbose_name='Context'),
        ),
        migrations.AlterField(
            model_name='email',
            name='headers',
            field=jsonfield.fields.JSONField(blank=True, null=True, verbose_name='Headers'),
        ),
        migrations.AlterField(
            model_name='email',
            name='priority',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'low'), (1, 'medium'), (2, 'high'), (3, 'now')], null=True, verbose_name='Priority'),
        ),
        migrations.AlterField(
            model_name='email',
            name='scheduled_time',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='The scheduled sending time'),
        ),
        migrations.AlterField(
            model_name='email',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'sent'), (1, 'failed'), (2, 'queued')], db_index=True, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='email',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post_office.EmailTemplate', verbose_name='Email template'),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='default_template',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translated_templates', to='post_office.EmailTemplate', verbose_name='Default template'),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='description',
            field=models.TextField(blank=True, help_text='Description of this template.', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='language',
            field=models.CharField(blank=True, default='', help_text='Render template in alternative language', max_length=12, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='name',
            field=models.CharField(help_text="e.g: 'welcome_email'", max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='log',
            name='email',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='post_office.Email', verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='log',
            name='exception_type',
            field=models.CharField(blank=True, max_length=255, verbose_name='Exception type'),
        ),
        migrations.AlterField(
            model_name='log',
            name='message',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='log',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'sent'), (1, 'failed')], verbose_name='Status'),
        ),
    ]
