# Generated by Django 2.2.7 on 2019-11-21 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0002_remove_webhook_remote_port'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webhook',
            old_name='post_data',
            new_name='data',
        ),
        migrations.AddField(
            model_name='webhook',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
