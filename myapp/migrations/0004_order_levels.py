# Generated by Django 3.0.7 on 2020-06-21 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200620_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='levels',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
