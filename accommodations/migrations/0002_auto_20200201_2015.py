# Generated by Django 2.2.9 on 2020-02-01 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accommodations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accommodationprice',
            old_name='price',
            new_name='daily_price',
        ),
    ]
