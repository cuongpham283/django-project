# Generated by Django 2.1.2 on 2018-11-06 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deliverynowapp', '0005_orderdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deliverynowapp.Driver'),
        ),
    ]
