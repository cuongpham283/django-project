# Generated by Django 2.1.2 on 2018-11-14 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliverynowapp', '0011_auto_20181113_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='location',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
