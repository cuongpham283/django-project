# Generated by Django 2.1.2 on 2018-11-04 17:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deliverynowapp', '0003_meal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('total', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'Cooking'), (2, 'Ready'), (3, 'Ontheway'), (4, 'Delivered')])),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('picked_at', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliverynowapp.Customer')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliverynowapp.Driver')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliverynowapp.Restaurant')),
            ],
        ),
    ]
