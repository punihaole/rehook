# Generated by Django 2.2.7 on 2019-11-11 01:42

import django.contrib.postgres.fields.hstore
import django.contrib.postgres.fields.jsonb
from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations, models
import webhook.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='Webhook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme', models.CharField(blank=True, max_length=8, null=True)),
                ('path', models.CharField(max_length=255)),
                ('method', models.CharField(blank=True, max_length=8, null=True)),
                ('query_params', models.CharField(blank=True, max_length=255)),
                ('remote_address', models.CharField(max_length=45)),
                ('remote_port', models.IntegerField()),
                ('remote_host', models.CharField(blank=True, max_length=255, null=True)),
                ('headers', django.contrib.postgres.fields.hstore.HStoreField()),
                ('encoding', models.CharField(blank=True, max_length=255, null=True)),
                ('post_data', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('date', models.DateTimeField(auto_now=True, db_index=True)),
                ('rehook_id', webhook.fields.Base36IntegerField(db_index=True, prefix='wh_', unique=True)),
            ],
        ),
    ]
