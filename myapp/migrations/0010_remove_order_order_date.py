# Generated by Django 3.0.8 on 2020-07-20 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200720_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
    ]
