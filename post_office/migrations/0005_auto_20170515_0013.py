# Generated by Django 1.11.1 on 2017-05-15 00:13
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_office', '0004_auto_20160607_0901'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='emailtemplate',
            unique_together=set([('name', 'language', 'default_template')]),
        ),
    ]
