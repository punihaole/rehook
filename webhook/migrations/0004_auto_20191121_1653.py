# Generated by Django 2.2.7 on 2019-11-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0003_auto_20191121_0746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='webhook',
            options={'ordering': ('-date',)},
        ),
        migrations.AddField(
            model_name='webhook',
            name='body_raw',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]