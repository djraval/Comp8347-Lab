# Generated by Django 3.0.7 on 2020-06-21 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='levels',
            field=models.PositiveIntegerField(),
        ),
    ]
